from flask import Flask, render_template
import pandas as pd

app = Flask(__name__, static_url_path='/static')

# Load the dataset
data = pd.read_csv("design_principles_coding.csv")

@app.route('/')
def index():
    return render_template('index_1.html', data=data)

@app.route('/detail/<int:index>')
def detail(index):
    principle = data.iloc[index]  # Retrieve the design principle based on the index
    return render_template('detail.html', principle=principle)

if __name__ == '__main__':
    app.run(debug=True)
