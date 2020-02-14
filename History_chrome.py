import pandas as pd
import numpy as np

# Open our file
with open('hist.txt') as f:
    content = f.readlines()
# Strip whitespace then split on first occurrence of pipe character
raw_data = [line.split('|', 1) for line in [x.strip() for x in content]]
# We now have a 2D list.
data = pd.DataFrame(raw_data, columns=['datetime', 'url'])
data.datetime = pd.to_datetime(data.datetime)

print(data.head(1))
print(data.datetime[0])
