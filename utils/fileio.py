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