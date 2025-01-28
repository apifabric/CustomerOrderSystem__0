
from logic_bank.logic_bank import Rule
from database.models import *

def init_rule():
  Rule.formula(derive=Item.amount, as_expression=lambda row: row.quantity * row.unit_price)
