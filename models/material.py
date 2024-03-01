# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Material(models.Model):
    _name = 'gestion_eventos.material'
    _description = 'Fase'

    code = fields.Char(string='Código')
    name = fields.Char(string='Name', required=True)
    type = fields.Selection([('L','LIGHTS'), ('S','SOUND'),('M','MOUNT'),('EL','ELECTRICAL'),('G','GRIPS'),
                             ('GR','GENERAL RESOURCES'),('O', 'OTHERS')], required=True)
    
    provider_id = fields.Many2one('res.partner', string='Proveedor', domain=[('supplier_rank', '!=', 0)])
    provider_phone = fields.Char(string="Teléfono del proveedor", compute="_compute_provider_phone")
    provider_address = fields.Char(stirng="Dirección del proveedor", compute="_compute_provider_address")

    cost_price = fields.Float(string='Precio de coste')
    pvp = fields.Float(string='PVP')

    _sql_constraints = [
        ('unique_code','unique(code)','Code and type must be unique.')
    ]

    @api.depends('provider_id')
    def _compute_provider_phone(self):
        self.provider_phone = self.provider_id.phone
    
    @api.depends('provider_id')
    def _compute_provider_address(self):
        self.provider_address = self.provider_id.street