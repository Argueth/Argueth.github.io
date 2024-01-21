# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Fase(models.Model):
    _name = 'gestion_eventos.material'
    _description = 'Fase'

    code = fields.Integer(required=True)
    name = fields.Char(string='Name', required=True)
    type = fields.Selection([('L','LIGHTS'), ('S','SOUND'),('M','MOUNT'),('EL','ELECTRICAL'),('G','GRIPS'),
                             ('GR','GENERAL RESOURCES')], required=True)

    event_id = fields.Many2one('gestion_eventos.event')

    _sql_constraints = [
        ('unique_code','unique(code)','Code must be unique.')
    ]

    

            
