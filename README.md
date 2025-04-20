# AI Sentiment Analysis API QA

This project performs automated testing on a free sentiment analysis model using a public API from Hugging Face. It validates classification accuracy, latency, and edge case handling.

## Tools Used
- Python (Requests, PyTest)
- Postman (manual testing phase)
- Free Hugging Face API
- GitHub Actions (optional for CI)

## What We Test
- Classification for Positive, Negative, Neutral sentiments
- Response latency (performance)
- API behavior with edge cases (empty input, long text, special characters)

## Getting Started
1. Clone this repo
2. `pip install -r requirements.txt`
3. Run tests: `pytest tests/`

## Author
Ayooluwa Paul Obembe
