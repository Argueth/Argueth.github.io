# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Line(models.Model):
    _name = 'gestion_eventos.line'
    _description = 'Line'
    _rec_name = 'code'

    code = fields.Integer(string='Line number', required=True)
    concept_id = fields.Many2one('gestion_eventos.material', required=True)
    quantity = fields.Integer(string='Quantity', default=0, required=True)
    init_price = fields.Float(string='Precio Inicial', related='concept_id.pvp')
    price = fields.Float(string='Precio', compute='_calculate_total_price')

    budget_id = fields.Many2one('gestion_eventos.budget', string='Presupuesto')

    _sql_constraints = [
        ('unique_identity','unique(code,budget_id)','Line number must be unique.')
    ]
    
    @api.depends('quantity', 'init_price')
    def _calculate_total_price(self):
        for r in self:
            r.price = r.quantity * r.init_price
"""
    @api.depends('concept_id')
    def _compute_init_price(self):
        for record in self:
            record.init_price = record.concept_id.pvp if record.concept_id else 0.0
"""

