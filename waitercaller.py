from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def home():
    return "Under construction"

if __name__ == '__main__':
  app.run(port=8000, debug=True)