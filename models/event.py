# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Event(models.Model):
    _name = 'gestion_eventos.event'
    _description = 'Event'

    code = fields.Integer(required=True)
    name = fields.Char(string='Event', required=True)
    start_date = fields.Date()
    end_date = fields.Date()

    customer_id = fields.Many2one('res.partner', string='Cliente', domain=[('customer_rank', '!=', 0)], required=True)
    customer_phone = fields.Char(string='Teléfono del Cliente')
    customer_address = fields.Char(string='Dirección del Cliente')

    type_id = fields.Many2one('gestion_eventos.type',string='Tipo de evento')
    fases_id = fields.One2many('gestion_eventos.fase','code')
    budget_ids = fields.Many2many('gestion_eventos.budget_event', string='Presupuestos')

    last_budget_light_material_ids = fields.Many2many('gestion_eventos.material', string='Materiales de iluminación', compute='_compute_last_budget_light_material_ids')
    last_budget_sound_material_ids = fields.Many2many('gestion_eventos.material', string='Materiales de sonido', compute='_compute_last_budget_sound_material_ids')
    last_budget_mount_material_ids = fields.Many2many('gestion_eventos.material', string='Materiales de montaje', compute='_compute_last_budget_mount_material_ids')

    _sql_constraints = [
        ('unique_code','unique(code)','Code must be unique.')
    ]

    @api.onchange('customer_id')
    def _onchange_customer_id(self):
        if self.customer_id:
            self.customer_phone = self.customer_id.phone
            self.customer_address = self.customer_id.street
    
    @api.depends('budget_ids')
    def _compute_last_budget_light_material_ids(self):
        for event in self:
            # Obtengo el último presupuesto
            last_budget = event.budget_ids[-1:]
            if last_budget:
                # Obtengo las líneas del último presupuesto
                last_budget_lines = last_budget.line_ids
                # Filtro las líneas para obtener solo los materiales de un tipo concreto
                materials = last_budget_lines.filtered(lambda line: line.concept_id.type in ['L', 'O']).mapped('concept_id')
                # Asigno los materiales al campo last_budget_material_ids
                event.last_budget_light_material_ids = [(6, 0, materials.ids)]
            else:
                event.last_budget_light_material_ids = False
    
    @api.depends('budget_ids')
    def _compute_last_budget_sound_material_ids(self):
        for event in self:
            # Obtengo el último presupuesto
            last_budget = event.budget_ids[-1:]
            if last_budget:
                # Obtengo las líneas del último presupuesto
                last_budget_lines = last_budget.line_ids
                # Filtro las líneas para obtener solo los materiales de un tipo concreto
                materials = last_budget_lines.filtered(lambda line: line.concept_id.type in ['S', 'O']).mapped('concept_id')
                # Asigno los materiales al campo last_budget_material_ids
                event.last_budget_sound_material_ids = [(6, 0, materials.ids)]
            else:
                event.last_budget_sound_material_ids = False

    @api.depends('budget_ids')
    def _compute_last_budget_mount_material_ids(self):
        for event in self:
            # Obtengo el último presupuesto
            last_budget = event.budget_ids[-1:]
            if last_budget:
                # Obtengo las líneas del último presupuesto
                last_budget_lines = last_budget.line_ids
                # Filtro las líneas para obtener solo los materiales de un tipo concreto
                materials = last_budget_lines.filtered(lambda line: line.concept_id.type in ['M', 'O']).mapped('concept_id')
                # Asigno los materiales al campo last_budget_material_ids
                event.last_budget_mount_material_ids = [(6, 0, materials.ids)]
            else:
                event.last_budget_mount_material_ids = False



    
