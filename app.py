from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def index():
    # Fetch message from the backend API
    response = requests.get("http://localhost:3001/api/message")
    message = response.json().get("message", "No message from backend.")
    return render_template("index.html", message=message)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
