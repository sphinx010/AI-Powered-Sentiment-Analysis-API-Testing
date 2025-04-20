import requests
import time

API_URL = "https://api-inference.huggingface.co/models/cardiffnlp/twitter-roberta-base-sentiment"
HEADERS = {"Authorization": "Bearer YOUR_HF_API_KEY"}

def test_latency():
    start = time.time()
    response = requests.post(API_URL, headers=HEADERS, json={"inputs": "I love this!"})
    end = time.time()
    assert (end - start) < 1.5  # seconds
