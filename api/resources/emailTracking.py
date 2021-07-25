from flask import jsonify, request
from flask_restful import Resource

import pandas as pd
import re
import json

regex_list = [
    "3S[A-Z]{4}[0-9]{6,9}", # PostNL 3S Tracking Number
    "(LA|UE|C[A-Z]|RI)[0-9]{9}NL", # PostNL EU Tracking Number
    "JVGL[0-9]{15,20}", # DHL Tracking Number
    "[0-9]{14}", # DPD Tracking Number
    #"[0-9]\.[0-9]{3,5}E\+12" # DPD Temporary Fix Tracking Number
]

compiled_regex = re.compile('|'.join(regex_list))

class EmailTracking(Resource):
    def post(self):
        # accepts JSON data from client
        email_data = request.get_json() # returns None if request is not json
        if email_data is None:
            return "Failed Parsing input. Accepts JSON.", 400

        try:
            subject = email_data['subject']
            body = email_data['body']
        except KeyError:
            return "Failed Parsing JSON. 'subject' and 'body' keys are required.", 400

        if not isinstance(subject, str) or not isinstance(body, str):
            return "Failed Parsing JSON. 'subject' and 'body' must be strings.", 400
        
        str_to_parse = (subject + " " + body).upper()

        tracking_number_match = re.search(compiled_regex, str_to_parse)
        if tracking_number_match is None:
            return "No valid tracking number found in email.", 400
        
        tracking_number = tracking_number_match.group(0)

        df = pd.read_csv("parcel_data.csv")

        parcel_info_series = df.loc[df['tracking_number'] == tracking_number]
        if parcel_info_series.empty:
            return "No parcel found with tracking number: " + tracking_number, 400
        
        parcel_info = json.loads(parcel_info_series.to_json(orient='records'))[0]


        return parcel_info, 200