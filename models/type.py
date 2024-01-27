# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Type(models.Model):
    _name = 'gestion_eventos.type'
    _description = 'Type'

    code = fields.Integer(string='Código', required=True)
    name = fields.Char(string='Nombre', required=True)

    description = fields.Text(string='Descripción')
    budget_ids = fields.Many2many('gestion_eventos.budget', string='Presupuestos')
    price = fields.Float(compute='_compute_total_price', string='Precio')
    _sql_constraints = [
        ('unique_code','unique(code)','Code must be unique.'),
        ('unique_name','unique(name)','Name must be unique.')
    ]

    @api.depends('budget_ids.total_price')
    def _compute_total_price(self):
        for record in self:
            record.price = sum(record.budget_ids.mapped('total_price'))
