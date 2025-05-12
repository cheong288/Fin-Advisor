from flask import Flask, request, render_template
import google.generativeai as genai
import os

app = Flask(__name__)

api = 'AIzaSyA6xgtZd1jSdu9Rf1jg0xTK5mYSjw6eKK0'

genai.configure(api_key=api)
model = genai.GenerativeModel("gemini-pro")

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
