# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Line(models.Model):
    _name = 'gestion_eventos.line'
    _description = 'Line'
    _rec_name = 'code'

    code = fields.Integer(string='Numero de línea', required=True)
    concept = fields.Selection(selection='_get_materials', string='Concepto', required=True)
    quantity = fields.Integer(string='Cantidad', default=0, required=True)
    unity_price = fields.Float(string='Precio Unitario', compute='_compute_unity_price', required=True)
    price = fields.Float(string='Precio', compute='_calcule_total_price', required=True)

    budget_id = fields.Many2one('gestion_eventos.budget', string='Presupuesto')

    _sql_constraints = [
        ('unique_identity','unique(code, budget_id)','Line number must be unique.')
    ]

    @api.model
    def _get_materials(self):
        material_records = self.env['gestion_eventos.material'].search([])
        return [(str(material.code), material.name) for material in material_records]
    
    @api.depends('concept')
    def _compute_unity_price(self):
        for record in self:
            if self.concept:
                record.unity_price = self.concept.price
            else:
                record.unity_price = 0.0


    @api.depends('quantity', 'unity_price')
    def _calcule_total_price(self):
        for r in self:
            r.price = r.quantity * r.unity_price
