# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Budget_Template(models.Model):
    _name = 'gestion_eventos.budget_template'
    _description = 'Budget_Template'

    _inherit = 'gestion_eventos.budget_abstract'