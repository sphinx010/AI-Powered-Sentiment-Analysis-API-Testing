import requests

API_URL = "https://api-inference.huggingface.co/models/cardiffnlp/twitter-roberta-base-sentiment"
HEADERS = {"Authorization": "Bearer YOUR_HF_API_KEY"}

def test_empty_text():
    response = requests.post(API_URL, headers=HEADERS, json={"inputs": ""})
    assert response.status_code == 200
    assert "label" in str(response.json())

def test_special_characters():
    response = requests.post(API_URL, headers=HEADERS, json={"inputs": "@@@##$%^&*()"})
    assert response.status_code == 200
