from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return "This is the home page, ok"
    
if __name__ == "__main__":
    app.run(debug=True)