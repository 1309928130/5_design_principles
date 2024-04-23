from flask import Flask, render_template
import pandas as pd

# app = Flask(__name__)
# app = Flask(__name__, static_folder='static')
# app = Flask(__name__, static_url_path='/Users/enshanchen/Desktop/Thesis_folder/5_design_principles/static/')
app = Flask(__name__, static_url_path='/static')


# Load the dataset
data = pd.read_csv("design_principles_coding.csv")

@app.route('/')
def index():
    return render_template('index_1.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
