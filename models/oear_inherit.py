# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.addons.budget_core.models.utilities import choices_tuple


class TaskInherit(models.Model):
    _inherit = 'budget.opex.oear'

    # CHOICES
    # ----------------------------------------------------------

    # BASIC FIELDS
    # ----------------------------------------------------------

    # RELATIONSHIPS
    # ----------------------------------------------------------
    po_id = fields.Many2one('budget.invoice.purchase.order',
                            string='Purchase Order')

    actual_ids = fields.One2many('budget.invoice.actual',
                                'oear_id',
                                string="Actuals")

    # COMPUTE FIELDS
    # ----------------------------------------------------------

    # BUTTONS
    # ----------------------------------------------------------
