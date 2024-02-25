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
            conflicting_event_info = ""
            if record.employee_ids and record.event_ids:
                # Obtenemos las fechas del evento actual
                current_event_start_date = record.event_ids.start_date
                current_event_end_date = record.event_ids.end_date

                # Buscamos otros eventos donde este empleado esté asignado en las mismas fechas
                conflicting_events = self.env['gestion_eventos.event'].search([
                    ('id', '!=', record.event_ids.id),  # Excluir el propio evento actual
                    ('start_date', '<=', current_event_end_date),
                    ('end_date', '>=', current_event_start_date),
                    ('employee_light_ids', 'in', record.employee_ids.ids),  # Ajusta esto según tu modelo
                ])

                if conflicting_events:
                    for event in conflicting_events:
                        duration = min(event.end_date, current_event_end_date) - max(event.start_date, current_event_start_date)
                        conflicting_event_info += f"\nEvento: {event.name}, Duración del conflicto: {duration.days} días"

            record.conflicting_event_info = conflicting_event_info