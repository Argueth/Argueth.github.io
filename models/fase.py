# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Fase(models.Model):
    _name = 'gestion_eventos.fase'
    _description = 'Fase'

    name = fields.Char(string='Fase', required=True)
    description = fields.Text(string='Descripción')
    start_date = fields.Datetime(string='Fecha de inicio')
    end_date = fields.Datetime(string="Fecha de fin")

    event_id = fields.Many2one('gestion_eventos.event')

    _sql_constraints = [
        ('unique_code','unique(name, event_id)','Code must be unique.')
    ]