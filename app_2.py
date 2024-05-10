from flask import Flask, render_template, request, jsonify
import pandas as pd
import os

app = Flask(__name__, static_url_path='/static')

# Load the dataset
data1 = pd.read_csv("design_principles_coding.csv", delimiter=";")

# Sort the data by the 'index' column
data1.sort_values(by='index', inplace=True)

data = data1

@app.route('/design_principle_detail/<int:principle_id>')
def design_principle_detail(principle_id):
    # Assuming you have logic to retrieve the filenames from the folder
    folder_path = f"static/detail_pictures_folder/{principle_id}"  # Path to the folder containing images for the principle
    image_files = os.listdir(folder_path)  # Get a list of all filenames in the folder

    return render_template('design_principle_detail.html', image_files=image_files)


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

    # Get list of image filenames and their descriptions
    folder_path = f"static/image/{principle['detail_pictures_folder']}"
    image_files = [f for f in os.listdir(folder_path) if f.endswith('.jpeg') or f.endswith('.jpg') or f.endswith('.png')]
    descriptions = []

    # Read the description CSV file
    description_csv_path = os.path.join(folder_path, 'description.csv')
    if os.path.exists(description_csv_path):
        description_df = pd.read_csv(description_csv_path)
        image_descriptions = dict(zip(description_df['filename'], description_df['description']))
    else:
        image_descriptions = {}

    return render_template('detail_2.html', principle=principle, image_files=image_files, image_descriptions=image_descriptions, data=data)


@app.route('/rearrange', methods=['POST'])
def rearrange():
    new_order = request.json['newOrder']  # Get the new order of design principles
    updated_data = data.iloc[new_order]  # Rearrange the data according to the new order
    return updated_data.to_json(orient='records')

@app.route('/get_available_themes')
def get_available_themes():
    # Extract all unique themes from the '(Other) Themes' column
    available_themes = set()
    for themes_str in data['(Other) Themes']:
        themes = themes_str.split('/')
        available_themes.update(themes)
    # return jsonify(list(available_themes))
    return list(available_themes)


@app.route('/filter_by_theme', methods=['POST'])
def filter_by_theme():
    selected_theme = request.json['theme']  # Get the selected theme
    filtered_principles = data[data['(Other) Themes'].str.contains(selected_theme)]

    return render_template('themes.html', data=filtered_principles, theme=selected_theme)


if __name__ == '__main__':
    app.run(debug=True)
