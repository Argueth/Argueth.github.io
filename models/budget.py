# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Budget(models.Model):
    _name = 'gestion_eventos.budget'
    _description = 'Budget'

    code = fields.Integer(string='Código', required=True)
    name = fields.Char(string='Nombre', required=True)
    total_price = fields.Float(string='Precio', compute='calcule_total_price', store=True)
    
    line_ids = fields.One2many('gestion_eventos.line', 'code')

    _sql_constraints = [
        ('unique_code','unique(code)','Code must be unique.'),
        ('unique_name','unique(name)','Name must be unique.')
    ]

    @api.depends('line_ids')
    def calcule_total_price(self):
        for r in self:
            r.total_price = 0
            for line in r.line_ids:
                r.total_price += line.price
