# -*- coding: utf-8 -*-

from odoo import models, fields, api

class EmployeesRel(models.Model):
    _name="gestion_eventos.employees_rel"
    _description="Empleados de iluminación"

    employee_ids = fields.Many2one('hr.employee')
    event_ids = fields.Many2one('gestion_eventos.event')

    employee_name = fields.Char(string="Nombre", related='employee_ids.name')
    department_id = fields.Many2one('hr.department', string="Departamento", related='employee_ids.department_id')
    conflicting_event_info = fields.Char(string="Evento en conflicto", compute='_compute_conflicting_event_info')

    _sql_constraints = [
        ('unique_combination','unique(employee,event)','Employee plus event combination must be unique.')
    ]

    @api.depends('employee_ids', 'event_ids')
    def _compute_conflicting_event_info(self):
        for record in self:
            conflicting_events = self.env['gestion_eventos.event'].search([
                ('id', '!=', record.event_ids.id),  # Evito el evento actual
                ('start_date', '<=', record.event_ids.end_date),  # El evento empieza antes de que termine el otro
                ('end_date', '>=', record.event_ids.start_date),  # El evento termina depués de que empiece el otro
            ])
            if conflicting_events:
                conflicting_names = ', '.join(conflicting_events.mapped('name'))
                record.conflicting_event_info = conflicting_names
            else:
                record.conflicting_event_info = 'No hay eventos en conflicto.'