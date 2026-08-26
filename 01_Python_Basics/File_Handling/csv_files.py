import csv
import io
# create a CSV sample in memory
csv_data = """Year, Industry, Value
2014, Manufacturing, 100000
2015, Construction, 200000
2016, Service, 300000
"""
csvfile = io.StringIO(csv_data)
csvreader = csv.reader(csvfile)
for row in csvreader:
    print(row)