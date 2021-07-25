# sendcloud-trackingAPI
Trial day assignment @ SendCloud

## Installation:
1. Setup virtual environment and install required packages with ```pip3```:
```
python3 -m venv venv
pip3 install .
```

2. Unzip encrypted parcel data .csv (same password as sent in email):
```
cd api
unzip parcel_data.zip
```

## Running/Testing the API
1a. Run API:
In api/ directory run:
```
flask run
```

1b. Test API:
In /test directory run:
```
pytest
```

## Additional Utils:
In the /utils directory two files are provided:
1. regexTester.py: Tests coverage of tracking numbers defined in the .csv file against API regex list
2. requests.py: Requires API running (see above). Creates multiple requests from provided tickets and outputs responses.
