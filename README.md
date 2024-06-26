# Design Principles for Demand-Responsive Station Areas
# Welcom!
 
<!DOCTYPE html>
<html>
<head>
    <title>Design Principles</title>
    <style>

@import url('https://fonts.googleapis.com/css2?family=Poppins:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,100;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&family=Roboto:ital,wght@0,100;0,300;0,400;0,500;0,700;0,900;1,100;1,300;1,400;1,500;1,700;1,900&display=swap');

<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Roboto:ital,wght@0,100;0,300;0,400;0,500;0,700;0,900;1,100;1,300;1,400;1,500;1,700;1,900&display=swap" rel="stylesheet">

@font-face {
    font-family: 'helvetica';
    src: url('helvetica-255/Helvetica.ttf') format('truetype');
    /* Add other properties such as font-weight and font-style if needed */
}

@font-face {
    font-family: 'helvetica-light';
    src: url('static/helvetica-255/helvetica-light-587ebe5a59211.ttf') format('truetype');
}

@font-face {
    font-family: 'helvetica-rounded-bold';
    src: url('/Users/enshanchen/Desktop/Thesis_folder/5_design_principles/helvetica-255/helvetica-rounded-bold-5871d05ead8de.otf') format('opentype');
}


@font-face {
    font-family: 'helvetica-boldOblique';
    src: url('Helvetica-BoldOblique.ttf') format('truetype');
}



        /* Define CSS styles for the images */
        .principles-container {
            display: flex;
            flex-wrap: wrap; /* Allow pictures to wrap to the next line */
            gap: 5px; /* Adjust the gap between images */
            justify-content: flex-start;
            margin-top: 10px;
            margin-left: 20px;
        }

        .principles-row {
            display: flex;
            gap: 5px; /* Adjust the gap between images */
            align-items: flex-start;
        }

        .principle {
            position: relative;
            cursor: pointer;
        }

        .principle img {
            width: auto ; /* Adjust the width of the images */
            height: 100px; /* Automatically adjust height while maintaining aspect ratio */
            transition: transform 0.3s ease-in-out;
        }

        .principle:hover img {
            transform: scale(1.5); /* Scale up the image on hover */
        }

        .tooltip {
            position: absolute;
            bottom: 0;
            left: 50%;
            transform: translateX(-50%);
            background-color: rgba(255, 255, 255, 0.8);
            padding: 5px 5px; /* Increase horizontal padding for width and vertical padding for height */
            border: none;
<!--            border: 1px solid #ccc;-->
            border: none;
            border-radius: 5px;
            visibility: hidden;
            opacity: 0;
            transition: opacity 0.3s ease-in-out;
            width: 150px; /* Adjust the width */
            max-height: 150px; /* Limit the maximum height */
            overflow-y: auto; /* Enable vertical scrollbar if content exceeds max-height */

            font-size: 15px; /* Adjust the font size */
            color: rgb(0, 0, 0); /* Adjust the color */
            font-family: "Roboto",  sans-serif; /* Change the font type */
        }

        .principle:hover .tooltip {
            visibility: visible;
            opacity: 1;
        }

        .row-title {

            margin-bottom: 10px; /* Adjust the space between rows */
            margin-left: 0px;

            color: rgb(0, 0, 0); /* Adjust the color */
            font-family: "Roboto",  sans-serif; /* Change the font type */
            font-style: italic;
            font-weight: 500;
            font-size: 18px; /* Adjust the font size */

        }
        .row-title::first-letter {
            /* Capitalize the first letter */
            text-transform: uppercase;
        }


        .main-heading {
            text-align: center;

            font-family: "Roboto", sans-serif;
            font-weight: 150;
            font-style: normal; /* or italic */
            font-size: 60px;
            color: black;

            margin-top: 10px;
            margin-bottom: 10px; /* Adjust the margin bottom as needed */
        }

        .dropdown-container {
            display: flex; /* Use flexbox to align items */
            align-items: center; /* Center items vertically */
            justify-content: center;
            margin-bottom: 10px; /* Add margin below the container */
        }

        .dropdown-label {
            margin-right: 5px; /* Add space between label and dropdown */

            font-family: "Roboto", sans-serif;
            font-weight: 400;
            font-style: normal;
            font-size: 20px;
            color: black;
        }

        .dropdown-menu {
            border: 1px solid #000; /* Add a border */
            border-radius: 25px; /* Add rounded corners */
            width: auto; /* Set the width of the dropdown box */
            margin-right: 2px;

            font-family: "Roboto", sans-serif;
            font-weight: 400;
            font-style: normal;
            font-size: 18px;
            color: crimson;
        }



    </style>
</head>

<body>
    <h1 class="main-heading">Design Principles</h1>

    <!-- Container for the label and dropdown -->
    <div class="dropdown-container">
        <!-- Text label for the dropdown menu -->
        <span class="dropdown-label">Perspective:</span>

        <!-- Dropdown menu for selecting dimensions -->
        <select id="dimensionSelect" class="dropdown-menu">
            <option value="">All</option>
            {% for col in data.columns %}
                {% if col not in ['index', 'picture_location', 'design_principle_name'] %}
                    <option value="{{ col }}" {% if selected_dimension == col %}selected{% endif %}>{{ col }}</option>
                {% endif %}
            {% endfor %}
        </select>
    </div>

    <div class="principles-container" id="principles-container">
        {% if selected_dimension %}
            {% for group in groups %}
                <div class="row-container">
                    <div class="row-title">{{ data[selected_dimension].iloc[group[0]] }}</div>
                    <div class="principles-row">
                        {% for index in group %}
                            {% set row = data.iloc[index] %}
                            <div class="principle" id="principle{{ index }}" draggable="true" ondragstart="drag(event)">
                                <a href="{{ url_for('detail_2', index=index) }}" target="_blank">
                                    <img src="{{ url_for('static', filename=row['picture_location']) }}" alt="Picture">
                                    <div class="tooltip">
                                        <p>{{ row['design_principle_name'] }}</p>
                                        <p>{{ row['research_methodology'] }}</p>
                                        <!-- Add more relevant information here -->
                                    </div>
                                </a>
                            </div>
                        {% endfor %}
                    </div>
                </div>
            {% endfor %}
        {% else %}
            {% for index, row in data.iterrows() %}
                <div class="principle" id="principle{{ index }}" draggable="true" ondragstart="drag(event)">
                    <a href="{{ url_for('detail_2', index=index) }}" target="_blank">
                        <img src="{{ url_for('static', filename=row['picture_location']) }}" alt="Picture">
                        <div class="tooltip">
                            <p>{{ row['design_principle_name'] }}</p>
                            <p>{{ row['research_methodology'] }}</p>
                            <!-- Add more relevant information here -->
                        </div>
                    </a>
                </div>
            {% endfor %}
        {% endif %}
    </div>


    <script>
        function allowDrop(ev) {
            ev.preventDefault();
        }

        function drag(ev) {
            ev.dataTransfer.setData("text", ev.target.id);
        }

        function drop(ev) {
            ev.preventDefault();
            var data = ev.dataTransfer.getData("text");
            ev.target.appendChild(document.getElementById(data));
            var newOrder = [];
            var principles = document.getElementsByClassName("principle");
            for (var i = 0; i < principles.length; i++) {
                var id = principles[i].id.replace("principle", "");
                newOrder.push(parseInt(id));
            }
            // Send the new order to the server
            fetch('/rearrange', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ newOrder: newOrder })
            }).then(response => response.json())
            .then(data => console.log(data))
            .catch(error => console.error('Error:', error));
        }

        // Add event listener to handle dropdown selection
        document.getElementById('dimensionSelect').addEventListener('change', function() {
            var dimension = this.value;
            // Update the URL to reflect the selected dimension
            window.location.href = '/?dimension=' + dimension;
        });




    </script>
</body>
</html>
