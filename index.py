from flask import Flask, render_template

app = Flask(__name__)
setup_metrics(app)

@app.route('/')
def main():
    return render_template('main.html')

