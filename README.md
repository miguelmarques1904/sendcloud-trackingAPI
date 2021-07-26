# sendcloud-trackingAPI
Trial day assignment @ SendCloud

Flask-based RESTful API. Uses the flask-restful extension.
Tests done with pytest.

## Installation:
1. Setup virtual environment and install required packages with ```pip3```:
```
python3 -m venv venv
. venv/bin/activate
pip3 install .
```

2. Export required Flask environment variables:
```
. ./exports.sh
```

3. Unzip encrypted parcel data set (same password as the one sent in email):
```
cd api
unzip parcel_data.zip
```

## Running/Testing the API
1a. Run API (inside the /api folder):

```
flask run
```

1b. Test API with pytest: (inside the /tests folder)
```
pytest
```

## Additional Utils:
In the /utils directory two files are provided:
1. regexTester.py: Tests coverage of tracking numbers defined in the .csv file against the API's regex list.
2. requests.py: Requires API running (see above). Creates multiple requests from provided tickets and outputs response information.
