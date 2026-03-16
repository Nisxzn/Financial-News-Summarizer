
# 📈 EquitySum: AI Financial News Summarizer

EquitySum is a high-end, AI-powered tool designed to distill complex financial news and market reports into concise, actionable summaries. Using NLP models, it extracts the core insights from long-form articles, saving you time and improving market comprehension.

## ✨ Features

- **AI Summarization**: Powered by the Facebook BART-large-CNN model.
- **Modern UI**: Sleek, glassmorphic design optimized for focus.
- **Responsive**: Works seamlessly across different screen sizes.
- **Fast Performance**: Instant results with backend processing.

## 🚀 Getting Started

### 1. Prerequisites
Ensure you have Python 3.8+ installed.

### 2. Installation
Install the required dependencies:
```bash
pip install -r requirements.txt
```

### 3. Launching the Backend
Navigate to the backend directory and start the Flask server:
```bash
cd backend
python app.py
```
The server will start on `http://127.0.0.1:5000`.

### 4. Running the Frontend
Simply open `frontend/index.html` in your favorite web browser.

## 🛠 Technology Stack

- **Backend**: Python, Flask, HuggingFace Transformers (PyTorch)
- **Frontend**: HTML5, Vanilla CSS3 (Inter Font, Flexbox, Glassmorphism)
- **Model**: `facebook/bart-large-cnn`
