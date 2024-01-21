# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Event(models.Model):
    _name = 'gestion_eventos.event'
    _description = 'Event'

    code = fields.Integer(required=True)
    name = fields.Char(string='Event', required=True)
    type1 = fields.Char()
    type2 = fields.Char()
    type3 = fields.Char()
    start_date = fields.Date()
    end_date = fields.Date()

    fases_id = fields.One2many('gestion_eventos.fase','code')

    materials_id = fields.One2many('gestion_eventos.material', 'code')

    _sql_constraints = [
        ('unique_code','unique(code)','Code must be unique.')
    ]

    
