import csv
import argparse
import os

def extract_data_csv(file, x, y):
    if not os.path.isfile(file):
        print("File does not exist.")
        return

    try:
        with open(file, 'r') as csvfile:
            csv_reader = csv.reader(csvfile)
            data = list(csv_reader)
    except csv.Error:
        print("Failed to parse the CSV file.")
        return
    
    if x < 0 or y < 0 or x >= len(data) or y >= len(data[x]):
        print("Coordinates are out of range.")
        return
    
    print(data[x][y])

parser = argparse.ArgumentParser(description="Reads a CSV file and prints value at x-th row and y-th column.")
parser.add_argument("file", help="CSV file path")
parser.add_argument("x", type=int, help="Row index (starts from 0)")
parser.add_argument("y", type=int, help="Column index (starts from 0)")

args = parser.parse_args()
extract_data_csv(args.file, args.x, args.y)
