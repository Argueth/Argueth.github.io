# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Event(models.Model):
    _name = 'gestion_eventos.event'
    _description = 'Event'

    code = fields.Integer(required=True)
    name = fields.Char(string='Event', required=True)
    start_date = fields.Date(string="Fecha de inicio", required=True)
    end_date = fields.Date(string="Fecha de fin", required=True)

    event_status = fields.Selection([('0','Propuesta'), ('1','Aceptado'), ('2','Terminado')], required=True, default='0')

    customer_id = fields.Many2one('res.partner', string='Cliente', domain=[('customer_rank', '!=', 0)], required=True)
    customer_phone = fields.Char(string='Teléfono del Cliente')
    customer_address = fields.Char(string='Dirección del Cliente')

    type_id = fields.Many2one('gestion_eventos.type',string='Tipo de evento')
    fases_id = fields.One2many('gestion_eventos.fase','code')
    budget_ids = fields.Many2many('gestion_eventos.budget_event', string='Presupuestos')

    last_budget_light_line_ids = fields.Many2many('gestion_eventos.line', string='Materiales de iluminación', compute='_compute_last_budget_light_line_ids')
    last_budget_sound_line_ids = fields.Many2many('gestion_eventos.line', string='Materiales de sonido', compute='_compute_last_budget_sound_line_ids')
    last_budget_mount_line_ids = fields.Many2many('gestion_eventos.line', string='Materiales de montaje', compute='_compute_last_budget_mount_line_ids')
    
    employee_light_ids = fields.Many2many('gestion_eventos.hr_employee_custom', string='Empleados de iluminación', relation='gestion_eventos_employee_light_rel', widget="many2many_tags")
    employee_sound_ids = fields.Many2many('gestion_eventos.hr_employee_custom', string='Empleado de sonido', relation='gestion_eventos_employee_sound_rel', widget="many2many_tags")
    employee_mount_ids = fields.Many2many('gestion_eventos.hr_employee_custom', string='Empleados de montaje', relation='gestion_eventos_employee_mount_rel', widget="many2many_tags")

    _sql_constraints = [
        ('unique_code','unique(code)','Code must be unique.')
    ]

    def change_event_status(self):
        for event in self:
            if int(event.event_status) < 2:
                event.event_status = str(int(event.event_status)+1)
            else:
                event.event_status = '0'

    @api.onchange('customer_id')
    def _onchange_customer_id(self):
        if self.customer_id:
            self.customer_phone = self.customer_id.phone
            self.customer_address = self.customer_id.street
    
    @api.depends('budget_ids')
    def _compute_last_budget_light_line_ids(self):
        for event in self:
            # Obtengo el último presupuesto
            last_budget = event.budget_ids[-1:]
            if last_budget:
                # Obtengo las líneas del último presupuesto
                last_budget_lines = last_budget.line_ids
                # Filtro las líneas para obtener solo los materiales de un tipo concreto
                filtered_lines = last_budget_lines.filtered(lambda line: line.concept_id.type in ['L', 'O'])
                # Asigno los materiales al campo last_budget_material_ids
                event.last_budget_light_line_ids = [(6, 0, filtered_lines.ids)]
            else:
                event.last_budget_light_line_ids = False
    
    @api.depends('budget_ids')
    def _compute_last_budget_sound_line_ids(self):
        for event in self:
            # Obtengo el último presupuesto
            last_budget = event.budget_ids[-1:]
            if last_budget:
                # Obtengo las líneas del último presupuesto
                last_budget_lines = last_budget.line_ids
                # Filtro las líneas para obtener solo los materiales de un tipo concreto
                filtered_lines = last_budget_lines.filtered(lambda line: line.concept_id.type in ['S', 'O'])
                # Asigno los materiales al campo last_budget_material_ids
                event.last_budget_sound_line_ids = [(6, 0, filtered_lines.ids)]
            else:
                event.last_budget_sound_line_ids = False

    @api.depends('budget_ids')
    def _compute_last_budget_mount_line_ids(self):
        for event in self:
            # Obtengo el último presupuesto
            last_budget = event.budget_ids[-1:]
            if last_budget:
                # Obtengo las líneas del último presupuesto
                last_budget_lines = last_budget.line_ids
                # Filtro las líneas para obtener solo los materiales de un tipo concreto
                filtered_lines = last_budget_lines.filtered(lambda line: line.concept_id.type in ['M', 'O'])
                # Asigno los materiales al campo last_budget_material_ids
                event.last_budget_mount_line_ids = [(6, 0, filtered_lines.ids)]
            else:
                event.last_budget_mount_line_ids = False