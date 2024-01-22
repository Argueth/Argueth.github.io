# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Event(models.Model):
    _name = 'gestion_eventos.event'
    _description = 'Event'

    code = fields.Integer(required=True)
    name = fields.Char(string='Event', required=True)
    start_date = fields.Date()
    end_date = fields.Date()

    fases_id = fields.One2many('gestion_eventos.fase','code')
    materials_id = fields.One2many('gestion_eventos.material', 'code')
    type_id = fields.Selection(selection='_get_tipos', string='Tipo de evento', store=True)

    _sql_constraints = [
        ('unique_code','unique(code)','Code must be unique.')
    ]

    @api.model
    def _get_tipos(self):
        type_records = self.env['gestion_eventos.type'].search([])
        return [(type.code, type.name) for type in type_records]

    
