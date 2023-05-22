# Import Calculators
from utils import calculators

def test_calculate_monthly_debt_ratio():
  assert calculators.calculate_monthly_debt_ratio(1500, 4000) == 0.375

def test_calculate_loan_to_value_ratio():
  assert calculators.calculate_loan_to_value_ratio(210000, 250000) == 0.84