# app.py

from flask import Flask, request, jsonify
import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification
from utils import preprocess_text

app = Flask(__name__)

# Load model and tokenizer
model = AutoModelForSequenceClassification.from_pretrained("results")
tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    text = preprocess_text(data.get('tweet_text', ''))
    encoding = tokenizer(text, return_tensors='pt')
    with torch.no_grad():
        outputs = model(**encoding)
    logits = outputs.logits
    prediction = logits.argmax(-1).item()
    return jsonify({"prediction": prediction})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
