
from flask import Flask, request, jsonify
from flask_cors import CORS
from transformers import pipeline

app = Flask(__name__)
CORS(app) # Enable CORS for all routes

# Load pretrained summarization model
# Note: This might take a while on first run
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

@app.route("/summarize", methods=["POST"])
def summarize():
    try:
        data = request.json
        if not data:
            return jsonify({"error": "No data provided"}), 400
            
        article = data.get("article", "")

        if not article or len(article.strip()) < 50:
            return jsonify({"summary": "Please provide a longer article for summarization (at least 50 characters)."})

        # Summarize
        result = summarizer(article, max_length=150, min_length=40, do_sample=False)
        summary = result[0]["summary_text"]

        return jsonify({"summary": summary})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True, port=5000)
