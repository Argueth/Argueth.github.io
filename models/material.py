# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Material(models.Model):
    _name = 'gestion_eventos.material'
    _description = 'Fase'

    code = fields.Integer(string='Código')
    name = fields.Char(string='Name', required=True)
    type = fields.Selection([('L','LIGHTS'), ('S','SOUND'),('M','MOUNT'),('EL','ELECTRICAL'),('G','GRIPS'),
                             ('GR','GENERAL RESOURCES'),('O', 'OTHERS')], required=True)
    
    provider_id = fields.Many2one('res.partner', string='Proveedor', domain=[('supplier_rank', '!=', 0)])
    
    cost_price = fields.Float(string='Precio')
    pvp = fields.Float(string='PVP')

    _sql_constraints = [
        ('unique_code','unique(code)','Code and type must be unique.')
    ]

    def _compute_code(self):
        existing_codes = set(self.env['gestion_eventos.material'].mapped('code'))
        used_codes = set(existing_codes)
        
        # Busca códigos liberados (gaps en la secuencia)
        for i in range(1, max(existing_codes, default=0) + 2):
            if i not in existing_codes:
                self.code = i
                return

        # Si no hay códigos liberados, usa el siguiente número después del máximo existente
        self.code = max(used_codes, default=0) + 1

            
