"""Helper functions to load CSV data"""
from pathlib import Path
import csv

def load_csv(csvpath):
  """Reads CSV file from provided path returns list of rows"""
  with open(csvpath, "r") as csvfile:
    data = []
    csvreader = csv.reader(csvfile, delimiter=",")

    next(csvreader)

    for row in csvreader:
      data.append(row)
  return data

def save_csv(csvpath, data, header=None):
  """Saves the CSV file from path provided."""
  with open(csvpath, "w", newline="") as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=",")
    if header:
        csvwriter.writerow(header)
    csvwriter.writerows(data)