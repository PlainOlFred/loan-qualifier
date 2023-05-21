from pathlib import Path
import sys
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

  if not csvpath.exists():
    sys.exit(f"Can't find this path: {csvpath}")

  return load_csv(csvpath)

def get_applicant_info():
  credit_score = int(questionary.text("What's your credit score?").ask())
  debt = float(questionary.text("What's your current amount of monthly debt?").ask())
  income = float(questionary.text("What's your total monthly income?").ask())
  loan_amount = float(questionary.text("What's your desired loan amount?").ask())
  home_value = float(questionary.text("What's your home value?").ask())

  return credit_score, debt, income, loan_amount, home_value

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


def run():
  bank_data = load_bank_data()

  # Get the applicant's information
  credit_score, debt, income, loan_amount, home_value = get_applicant_info()

  # Find qualifying loans
  qualifying_loans = find_qualifying_loans(
      bank_data, credit_score, debt, income, loan_amount, home_value
  )

  print(qualifying_loans)
  
  return 0

if __name__ == "__main__":
  fire.Fire(run)