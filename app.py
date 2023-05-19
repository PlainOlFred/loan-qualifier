from pathlib import Path

from utils.fileio import load_csv

def load_bank_data(file_path):
  csvpath = Path(file_path)

  return load_csv(csvpath)


def run():
  bank_data = load_bank_data('./data/daily_rate_sheet.csv')
  print(bank_data)
  
  return 0

if __name__ == "__main__":
  run()