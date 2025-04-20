import requests

def test_sentiment_classification():
    url = "https://api-inference.huggingface.co/models/cardiffnlp/twitter-roberta-base-sentiment"
    headers = {"Authorization": "Bearer YOUR_HF_API_KEY"}

    test_texts = [
        ("I love this app!", "positive"),
        ("This is terrible", "negative"),
        ("It's okay", "neutral")
    ]

    for text, expected in test_texts:
        response = requests.post(url, headers=headers, json={"inputs": text})
        prediction = response.json()[0][0]["label"].lower()
        assert expected in prediction
