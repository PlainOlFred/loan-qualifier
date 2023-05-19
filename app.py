from pathlib import Path
import fire
import questionary

from utils.fileio import load_csv
from utils.calculators import (calculate_monthly_debt_ratio, calculate_loan_to_value_ratio)
from utils.filters.debt_to_income import filter_debt_to_income
from utils.filters.loan_to_value import filter_loan_to_value
from utils.filters.credit_score import filter_credit_score
from utils.filters.max_loan import filter_max_loan_size

def load_bank_data():
  file_path = questionary.text("Enter a file path to a rate-sheet (.csv):").ask()
  csvpath = Path(file_path)

  return load_csv(csvpath)

def find_qualifying_loans(bank_data, credit_score, debt, income, loan, home_value):
  # Calculate the monthly debt ratio
  monthly_debt_ratio = calculate_monthly_debt_ratio(debt, income)
  print(f"The monthly debt to income ratio is {monthly_debt_ratio:.02f}")

  # Calculate loan to value ratio
  loan_to_value_ratio = calculate_loan_to_value_ratio(loan, home_value)
  print(f"The loan to value ratio is {loan_to_value_ratio:.02f}.")

  # Filter Banks by qualifying requirements
  bank_data_filtered = filter_debt_to_income(monthly_debt_ratio, bank_data)
  bank_data_filtered = filter_loan_to_value(loan_to_value_ratio, bank_data_filtered)
  bank_data_filtered = filter_max_loan_size(loan, bank_data_filtered)
  bank_data_filtered = filter_credit_score(credit_score, bank_data_filtered)

  print(f"Found {len(bank_data_filtered)} qualifying loans")

  return bank_data_filtered


def run(credit_score, debt, income):
  bank_data = load_bank_data()

  # Set the applicant's information

  loan_amount = 100000
  home_value = 210000

  # Find qualifying loans
  qualifying_loans = find_qualifying_loans(
      bank_data, credit_score, debt, income, loan_amount, home_value
  )

  print(qualifying_loans)
  
  return 0

if __name__ == "__main__":
  fire.Fire(run)