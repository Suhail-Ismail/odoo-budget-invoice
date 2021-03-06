# -*- coding: utf-8 -*-

# INHERITANCE MODELS
# ----------------------------------------------------------
from . import budget_inherit, contract_inherit, contractor_inherit, \
    cear_inherit, oear_inherit, discount_rule_inherit, purchase_order_inherit

# BASIC MODELS
# ----------------------------------------------------------
from . import invoice, invoice_summary, invoice_amount, \
    invoice_cear_allocation, invoice_oear_allocation, \
    actual, invoice_volume_discount, project_estimated_cost

# SPECIAL MODELS
# ----------------------------------------------------------
from . import ir_autovacuum

# REPORT VIEW MODELS
# ----------------------------------------------------------
from . import cear_allocation_bi
