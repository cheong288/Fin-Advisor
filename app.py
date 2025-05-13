from flask import Flask, request, render_template
import google.generativeai as genai
import os
from dotenv import load_dotenv

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise EnvironmentError("GEMINI_API_KEY not found in .env file.")

app = Flask(__name__)

genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-1.5-flash")

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        user_input = request.form["prompt"]
        response = model.generate_content(user_input)
        result = response.text
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
