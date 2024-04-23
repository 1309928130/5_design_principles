from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__, static_url_path='/static')

# Load the dataset
data = pd.read_csv("design_principles_coding.csv")


@app.route('/')
def index():
    # Get the selected dimension from the query string
    selected_dimension = request.args.get('dimension')

    if selected_dimension is None or selected_dimension not in data.columns:
        # If no dimension selected or invalid dimension, render the default view
        return render_template('index_2.html', data=data, groups=[])

    # Group the design principles based on the selected dimension
    groups = []
    for value in data[selected_dimension].unique():
        group_indices = data[data[selected_dimension] == value].index.tolist()
        groups.append(group_indices)

    return render_template('index_2.html', data=data, groups=groups, selected_dimension=selected_dimension)


@app.route('/detail_2/<int:index>')
def detail_2(index):
    principle = data.iloc[index]  # Retrieve the design principle based on the index
    return render_template('detail_2.html', principle=principle)


@app.route('/rearrange', methods=['POST'])
def rearrange():
    new_order = request.json['newOrder']  # Get the new order of design principles
    updated_data = data.iloc[new_order]  # Rearrange the data according to the new order
    return updated_data.to_json(orient='records')


if __name__ == '__main__':
    app.run(debug=True)
