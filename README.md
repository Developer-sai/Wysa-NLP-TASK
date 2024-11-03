# Wysa-NLP-TASK

Emotion and Product Target Detection in Tweets
This project implements an NLP model to detect emotions in tweets and identify whether these emotions are directed toward specific products or brands. The solution includes data preprocessing, data augmentation, model training, and deployment as a web API using Flask and Docker, along with recommendations for monitoring metrics in a production environment.

Problem Statement
The primary objective of this project is to develop a solution capable of identifying emotions within tweets and determining if these emotions are directed toward specific brands or products. The requirements include:

Performing Exploratory Data Analysis (EDA)
Enhancing and augmenting the dataset for improved model performance
Fine-tuning a transformer-based model for emotion and target classification
Deploying the model as an API and ensuring post-deployment monitoring
Solution Overview
The project follows these major steps:

Data Preprocessing and EDA: Conducted initial data analysis and cleaning to understand and prepare the data.
Dataset Enhancement: Improved data quality by balancing classes and removing duplicate entries.
Data Augmentation: Applied techniques like synonym replacement, back translation, and random insertion to diversify the dataset.
Model Training: Fine-tuned a bert-base-uncased model to classify emotions and their targets.
Deployment: Created a Flask API with Docker for easy deployment, including configuration for AWS Elastic Beanstalk.
Monitoring and Metrics: Defined metrics for post-deployment monitoring to ensure the model’s performance remains robust.
Project Structure
plaintext
Copy code
emotion-product-detection/
│
├── data/
│   ├── Train.csv               # Training dataset
│   └── Test.csv                # Test dataset
│
├── notebooks/
│   ├── EDA.ipynb               # Exploratory Data Analysis notebook
│   └── Model_Training.ipynb    # Model training and evaluation notebook
│
├── app.py                      # Flask API for model inference
├── requirements.txt            # Project dependencies
├── Dockerfile                  # Docker configuration file
├── README.md                   # Project documentation
└── utils.py                    # Helper functions for data preprocessing and augmentation
Setup Instructions
Clone the Repository

git clone https://github.com/Developer-sai/emotion-product-detection.git
cd emotion-product-detection
Install Dependencies

Make sure you have Python 3.8 or later. Install project dependencies with:

pip install -r requirements.txt
Prepare the Dataset

Place Train.csv and Test.csv in the data/ folder.

Data
Train.csv: This file contains tweets with corresponding emotion labels and information about whether the emotion is directed toward a specific brand or product.
Test.csv: This file contains tweet texts for which you’ll generate predictions using the model.
Ensure that the dataset is correctly formatted and structured to avoid preprocessing errors.

Usage
Run EDA: Use the EDA.ipynb notebook to explore the data, visualize distributions, and preprocess it.

Data Augmentation and Model Training: Use Model_Training.ipynb to augment the dataset, fine-tune the transformer model, and evaluate the results.

Model Inference with Flask API: Start the Flask server with:

python app.py
API Endpoint: You can test the API by sending a POST request to the /predict endpoint:

curl -X POST -H "Content-Type: application/json" -d '{"tweet_text": "Sample tweet here"}' http://127.0.0.1:5000/predict
Deployment
Docker Deployment
Build Docker Image

docker build -t emotion-product-detection .
Run Docker Container

docker run -p 5000:5000 emotion-product-detection
AWS Elastic Beanstalk Deployment
Initialize Elastic Beanstalk

eb init -p docker emotion-product-detection
Create an Environment

eb create emotion-detection-env
Deploy the Application

eb deploy
Access the application by running:

eb open
Monitoring and Metrics
In production, monitor the following metrics to ensure the model’s performance and reliability:

Latency: Measure response time for each prediction request.
Throughput: Track the number of requests handled over time.
Error Rate: Monitor errors (e.g., HTTP 4XX or 5XX status codes) to diagnose potential issues.
Model Drift: Regularly evaluate model accuracy on new data to detect performance degradation.
Resource Usage: Track CPU, memory, and GPU utilization for optimization.
Future Enhancements
Potential future improvements for this project include:

Additional Data Sources: Incorporate more datasets to improve model robustness.
Advanced Data Augmentation: Experiment with more sophisticated data augmentation methods.
Automated Monitoring: Set up automated alerts for model drift and high resource usage.
License
This project is licensed under the MIT License - see the LICENSE file for details.
