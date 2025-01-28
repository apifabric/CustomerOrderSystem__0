import logging
from logic_bank.logic_bank import DeclareRule, Rule, LogicBank
from database.models import *
from decimal import Decimal
from datetime import date, datetime

log = logging.getLogger(__name__)

def declare_logic():
    """
        declare_logic - declare rules
        this function is called from logic/declare_logic.py
    """
    log.info("declare_logic - active rules")
    
    # Exported Rules:
    # Customer Balance Constraint 
    # Ensure that customer's balance is within the credit limit.
    Rule.constraint(validate=Customer, as_condition=lambda row: row.balance <= row.credit_limit, error_msg='Customer balance ({row.balance}) exceeds credit limit ({row.credit_limit})')
    
    # Customer Balance Summation 
    # Customer's balance is the sum of the order totals where the shipment date is null.
    Rule.sum(derive=Customer.balance, as_sum_of=Order.amount_total, where=lambda row: row.date_shipped is None)
    
    # Order Amount Total Summation 
    # Order's total amount is the sum of item amounts.
    Rule.sum(derive=Order.amount_total, as_sum_of=Item.amount)
    
    # Item Amount Calculation 
    # Item amount is calculated as quantity multiplied by unit price.
    Rule.formula(derive=Item.amount, as_expression=lambda row: row.quantity * row.unit_price)
    
    # Item Unit Price Copy 
    # Copy the unit price from the product to the item.
    Rule.copy(derive=Item.unit_price, from_parent=Product.unit_price)
    