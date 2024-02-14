# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Event(models.Model):
    _name = 'gestion_eventos.event'
    _description = 'Event'

    code = fields.Integer(required=True)
    name = fields.Char(string='Event', required=True)
    start_date = fields.Date()
    end_date = fields.Date()

    type_id = fields.Many2one('gestion_eventos.type',string='Tipo de evento')
    fases_id = fields.One2many('gestion_eventos.fase','code')
    budget_ids = fields.Many2many('gestion_eventos.budget_event', string='Presupuestos')

    _sql_constraints = [
        ('unique_code','unique(code)','Code must be unique.')
    ]


    
