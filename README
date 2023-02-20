# Brand branches lookup

This application is a web app designed to search a configurable brand name in a configurable radius from a given address

## Installation

Use the package manager pip (pip3) to install the project.

```bash
pip3 install -t requirements.txt
```

## Usage
Using the cli:
make sure to be run within the project root directory.

```
python app.py [--radius] [--brand_name]
```
Running with -h flag will explain all possible arguments.

## API endpoints:
1. GET request to "/" will be a sanity check that the app is running.
2. PUT request to "/configure_radius" with the query param "radius" as float will update the configurable variable radius.
3. PUT request to "/configure_brand_name" with the query param "brand_name" as string will update the configurable variable brand_name.
4. GET request to "/get_starbucks_in_radius" with the query param "address" as string will calculate all the branches of the "brand_name" distanced from the given address within the configurable "radius" variable

## API Response:
All API endpoints respond with a json stating {"success": true/false, ["reason"]}



## About the project

The project is a bit more generic than requested. You are able to search for any brand_name in any radius from the given address.

I chose to implement the app as a flask app for simplicity.
The db is in memory storage to avoid overhead of pulling data.
I chose to work with data frame from pandas library for efficiency after reading the following benchmark:

https://towardsdatascience.com/heres-the-most-efficient-way-to-iterate-through-your-pandas-dataframe-4dad88ac92ee

I chose to use a simple logger to indicate errors and regular actions.

Testing can be run by running:
```
pytest
```
The test and logger are quiet state forward and mainly act as framework for additional logging and testing to be added in the future.
