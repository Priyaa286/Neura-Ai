from flask import Flask, request, jsonify
import google.generativeai as genai
import os

app = Flask(__name__)

genai.configure(api_key=os.environ["GEMINI_API_KEY"])

model = genai.GenerativeModel(
    "gemini-1.5-flash",
    system_instruction="""
You are NeuroSig AI Assistant.

You help researchers understand:
- Participants
- EEG Recordings
- Substance History
- Addiction Predictions

Provide concise and professional answers.
You are not a medical diagnostic system.
"""
)

@app.route("/")
def home():
    return "Neura AI Backend Running"

@app.route("/chat", methods=["POST"])
def chat():

    data = request.get_json()

    question = data.get("message", "")

    response = model.generate_content(question)

    return jsonify({
        "answer": response.text
    })

if __name__ == "__main__":
    app.run()
