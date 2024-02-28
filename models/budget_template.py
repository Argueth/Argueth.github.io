# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Budget_Template(models.Model):
    _name = 'gestion_eventos.budget_template'
    _description = 'Budget_Template'

    _inherit = 'gestion_eventos.budget_abstract'

    line_ids = fields.One2many('gestion_eventos.line', 'budget_template_id', string='Líneas')

    @api.onchange('line_ids')
    def _onchange_line_ids(self):
        for i, line in enumerate(self.line_ids, start=1):
            line.code = i