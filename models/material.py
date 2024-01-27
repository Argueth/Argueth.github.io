# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Material(models.Model):
    _name = 'gestion_eventos.material'
    _description = 'Fase'

    code = fields.Integer(required=True)
    name = fields.Char(string='Name', required=True)
    type = fields.Selection([('L','LIGHTS'), ('S','SOUND'),('M','MOUNT'),('EL','ELECTRICAL'),('G','GRIPS'),
                             ('GR','GENERAL RESOURCES'),('O', 'OTHERS')], required=True)
    cost_price = fields.Float(string='Precio')
    pvp = fields.Float(string='PVP')

    _sql_constraints = [
        ('unique_code','unique(code)','Code and type must be unique.')
    ]

    

            
