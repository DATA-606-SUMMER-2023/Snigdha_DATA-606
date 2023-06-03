# Snigdha Chigurupati

# Data 606: Capstone project proposal

# Building a Recommendation System through the IMDB movie ratings

## Introduction
A recommender system is an algorithmic approach to provide personalized recommendations to users based on their preferences and interests. It analyzes user behavior, historical data, and item characteristics to suggest relevant items that the user might like or find useful. Recommender systems are widely used in various domains, such as e-commerce, streaming platforms, and content-based websites, to help users discover new items and enhance their overall experience by reducing the information overload and improving the relevance of recommendations.

## Project Overview
This project aims to develop a recommender system using the IMDb movie dataset from Kaggle. The recommender system will provide personalized movie recommendations to users, helping them discover relevant movies based on their preferences and the rich information available in the dataset.

## Dataset
This dataset from kaggle created by Ashish Jangra, is having the data of size, 661 MB.

Total observations: 2590932

Features:
- id - Movie ID
- name - Name of the Movie
- year - Year of movie release
- rating - Rating of the Movie
- certificate - Movie Certification
- duration - Duration of the Movie
- genre - Genre of the Movie
- votes - Number of people who voted for the IMDB rating
- gross_income - Gross Income of the Movie
- directors_id - ID of Directors who have worked on the movie
- directors_name - Name of the movie director
- stars_id - Star ID
- stars_name - Name of the stars in the movie
- description - Movie description

Unit of Analysis: Movies(IMDB ratings, votes, genre, stars, director, description)

Dataset link: https://www.kaggle.com/datasets/ashishjangra27/imdb-movies-dataset

## Research Interests and outcomes
To understand the choice of the users and develop an accurate and effective recommendation system that suggests relevant movies to users based on their preferences and historical movie ratings. The system aims to enhance the movie-watching experience by reducing information overload and assisting users in discovering movies they are likely to enjoy.

### Importance of the Issue:
This issue is important to both users and the movie industry. For users, the overwhelming number of movie choices makes it challenging to find movies that align with their tastes. A recommendation system helps users overcome this challenge by providing personalized recommendations, saving time and improving their overall movie-watching satisfaction. For the movie industry, a well-designed recommendation system can drive user engagement, increase movie discovery, and boost revenue through increased movie rentals, sales, or subscriptions.

### Questions to be answered:
- How to effectively capture and represent user preferences and movie characteristics to make accurate recommendations?
- Does cluserting techniques produce significant results?
- Which recommendation algorithms or models perform best on the IMDb movie ratings dataset, and how can their performance be evaluated?
- How to perform effective feature selection to incorporate factors such as movie genres, actors, directors, or release dates to enhance the relevance and diversity of recommendations?
- Is there a scope to build a prominent unsupervised model?
- How to handle the cold-start problem, where new users or movies have limited data available for recommendations?
- What is the impact of different recommendation strategies (e.g., collaborative filtering, content-based filtering) on the accuracy and user satisfaction of the system?
- How can we measure the effectiveness of the recommendation system using appropriate evaluation metrics?

### Project Implementation

#### Features to be used: 
name, year, rating, certificate, duration, genre, votes, gross_income, directors_name, stars_name, description

#### Implementation:
- Exploratory data analysis
- Data Cleaning: Removing the non-alphanumeric characters, converting the data into lowercase, Imputing the missing values
- Feature selection
- Data pre-processing: Vectorization, Clustering
- Recommendation techniques/ Model training(possible): Collaborative filtering, Content-based filtering, Hybrid approaches
- Model Evaluation: RMSE, F1-score, accuracy, Precision, Recall
- Hyperparameter tuning(possible): GridSearch, Cross validation
- Model Deployment(possible): Streamlit, Heroku, Flask

## Preliminary Analysis


## References
