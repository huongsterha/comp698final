from flask import Flask, render_template
from prometheus_metrics import setup_metrics

app = Flask(__name__)
setup_metrics(app)

@app.route('/')
def main():
    return render_template('main.html')
    
@app.route('/Gear')
def coffee():
    return render_template('gear.html')
    
@app.route('/Gear/Shoes')
def linktocoffee():
    return render_template('shoes.html')

if __name__== '__main__':
    app.run(debug=True,host='0.0.0.0',port=8080)
