from api.resources.emailTracking import compiled_regex

import pandas as pd
import re

df = pd.read_csv('../api/parcel_data.csv') # read parcel data

n_found = 0
n_matches = 0
# checks if every tracking number in the data set matches a defined regex
for track in df['tracking_number']:
    n_found += 1
    if not re.fullmatch(compiled_regex, track):
        print("Could not match:", track)
    else:
        n_matches += 1

print("Successfully matched", n_matches, "out of", n_found, "tracking numbers (", str(n_matches / n_found * 100) + "% )")
