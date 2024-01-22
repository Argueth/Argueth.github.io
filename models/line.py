# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Line(models.Model):
    _name = 'gestion_eventos.line'
    _description = 'Line'
    _rec_name = 'code'

    code = fields.Integer(string='Numero de línea', required=True)
    concept = fields.Char(string='Concepto', required=True)
    quantity = fields.Integer(string='Cantidad', default=0, required=True)
    unity_price = fields.Float(string='Precio Unitario', required=True)
    price = fields.Float(string='Precio', compute='_calcule_total_price', required=True)


    _sql_constraints = [
        ('unique_code','unique(code)','Code must be unique.'),
        ('unique_name','unique(concept)','Name must be unique.')
    ]

    @api.depends('quantity', 'unity_price')
    def _calcule_total_price(self):
        for r in self:
            r.price = r.quantity * r.unity_price
