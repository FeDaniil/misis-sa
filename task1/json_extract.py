import json
import argparse
import os
from jsonpath_ng import jsonpath, parse

def extract_data_json(file, xpath):
    if not os.path.isfile(file):
        print("File does not exist.")
        return

    try:
        with open(file, 'r') as jsonfile:
            data = json.load(jsonfile)
    except json.JSONDecodeError:
        print("Failed to parse the JSON file.")
        return

    try:
        jsonpath_expr = parse(xpath)
    except Exception as e:
        print("Failed to parse the XPath expression:", str(e))
        return

    matches = [match.value for match in jsonpath_expr.find(data)]

    for match in matches:
        print(match)

parser = argparse.ArgumentParser(description="Reads a JSON file and extracts data using XPath.")
parser.add_argument("file", help="JSON file path")
parser.add_argument("xpath", help="XPath expression")

args = parser.parse_args()

extract_data_json(args.file, args.xpath)
