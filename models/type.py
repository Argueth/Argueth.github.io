# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Type(models.Model):
    _name = 'gestion_eventos.type'
    _description = 'Type'

    code = fields.Integer(string='Código', required=True)
    name = fields.Char(string='Nombre', required=True)

    budget_id = fields.Selection(selection='_get_budget', string='Presupuesto')
    total_price = fields.Float(compute='_compute_total_price', string='Total Price', store=True)
    description = fields.Text(string='Descripción')

    _sql_constraints = [
        ('unique_code','unique(code)','Code must be unique.'),
        ('unique_name','unique(name)','Name must be unique.')
    ]

    @api.depends('budget_id')
    def _compute_total_price(self):
        for record in self:
            if record.budget_id:
                # Obtener el presupuesto seleccionado
                budget = self.env['gestion_eventos.budget'].browse(record.budget_id)

                # Asignar el precio total del presupuesto al campo total_price
                record.total_price = budget.total_price
            else:
                # Si no se selecciona un presupuesto, establecer el total_price en 0
                record.total_price = 0

    @api.model
    def _get_budget(self):
        budget_records = self.env['gestion_eventos.budget'].search([])
        return [(budget.code, budget.name) for budget in budget_records]