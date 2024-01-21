# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Fase(models.Model):
    _name = 'gestion_eventos.fase'
    _description = 'Fase'

    code = fields.Integer(required=True)
    name = fields.Char(string='Fase', required=True)
    start_date = fields.Date()
    end_date = fields.Date()

    event_id = fields.Many2one('gestion_eventos.event')

    _sql_constraints = [
        ('unique_code','unique(code)','Code must be unique.')
    ]