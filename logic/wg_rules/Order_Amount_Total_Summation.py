
from logic_bank.logic_bank import Rule
from database.models import *

def init_rule():
  Rule.sum(derive=Order.amount_total, as_sum_of=Item.amount)
