from flask import Flask, request, render_template
import numpy as np
import pandas as pd
import torch
from transformers import BertTokenizer, BertModel
from sklearn.metrics.pairwise import cosine_similarity
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
import string

app = Flask(__name__)

# Load the BERT model and tokenizer
model_name = 'bert-large-uncased'
tokenizer = BertTokenizer.from_pretrained(model_name)
model = BertModel.from_pretrained(model_name)

# Load movie data
movie_data = pd.read_csv("output_100.csv")
movie_embeddings = np.load("movie_embeddings.npy")

# Function to preprocess user input
def preprocess_user_input(text):
    words = text.lower().split()
    table = str.maketrans('', '', string.punctuation)
    words = [word.translate(table) for word in words if word.isalpha()]
    words = [word for word in words if word not in stopwords.words('english')]
    lemmatizer = WordNetLemmatizer()
    words = [lemmatizer.lemmatize(word) for word in words]
    preprocessed_text = ' '.join(words)
    return preprocessed_text

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_input = request.form['user_input']
        preprocessed_input = preprocess_user_input(user_input)

        # Tokenize and encode the new movie description
        encoded_new_movie = tokenizer.batch_encode_plus([preprocessed_input], add_special_tokens=True, padding='max_length', max_length=512, return_tensors='pt')
        new_input_ids = encoded_new_movie['input_ids']
        new_attention_mask = encoded_new_movie['attention_mask']

        # Generate BERT embeddings for the new movie description
        with torch.no_grad():
            model.eval()
            new_movie_embedding = model(new_input_ids, attention_mask=new_attention_mask)[0][:, 0, :].numpy()

        # Calculate cosine similarity between the new movie and existing movies
        similarity_scores = cosine_similarity(new_movie_embedding.reshape(1, -1), movie_embeddings)
        similar_movies_indices = np.argsort(similarity_scores[0])[::-1]

        # Get top similar movies
        top_similar_movies = movie_data.loc[similar_movies_indices[:10], ['name']]

        return render_template('index.html', user_input=user_input, similar_movies=top_similar_movies)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
