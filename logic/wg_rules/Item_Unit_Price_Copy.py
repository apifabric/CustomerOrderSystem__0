
from logic_bank.logic_bank import Rule
from database.models import *

def init_rule():
  Rule.copy(derive=Item.unit_price, from_parent=Product.unit_price)
