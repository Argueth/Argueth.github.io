# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Line(models.Model):
    _name = 'gestion_eventos.line'
    _description = 'Line'
    _rec_name = 'code'

    code = fields.Integer(string='Line number')
    concept_id = fields.Many2one('gestion_eventos.material', string="Concepto", required=True)
    init_price = fields.Float(string='Precio Inicial', related='concept_id.pvp')
    quantity = fields.Integer(string='Quantity', default=0, required=True)
    price = fields.Float(string='Precio de la línea', compute='_compute_total_price')

    budget_template_id = fields.Many2one('gestion_eventos.budget_template', string='Presupuesto')
    budget_event_id = fields.Many2one('gestion_eventos.budget_event', string='Presupuesto')

    _sql_constraints = [
        ('unique_identity','unique(code,budget_template_id,budget_event_id)','Line number must be unique.')
    ]
    
    @api.depends('quantity', 'init_price')
    def _compute_total_price(self):
        for r in self:
            r.price = r.quantity * r.init_price


