# -*- coding: utf-8 -*-

from odoo import models, fields, api

class EmployeeEventRel(models.Model):
    _name="gestion_eventos.employee_event_rel"
    _description="Empleados de iluminación"

    #name = fields.Char(string="Identificador")
    employee_id = fields.Many2one('hr.employee')
    event_id = fields.Many2one('gestion_eventos.event')

    employee_name = fields.Char(string="Nombre", related='employee_id.name')
    department_id = fields.Many2one('hr.department', string="Departamento", related='employee_id.department_id')
    conflicting_event_info = fields.Char(string="Evento en conflicto", compute='_compute_conflicting_event_info')

    _sql_constraints = [
        ('unique_combination','unique(employee,event)','Employee plus event combination must be unique.')
    ]

    @api.depends('employee_id', 'event_id')
    def _compute_conflicting_event_info(self):
        for record in self:
            conflicting_events = self.env['gestion_eventos.event'].search([
                #('id', '!=', record.event_id.id),  # Evito el evento actual
                ('start_date', '<=', record.event_id.end_date),  # El evento empieza antes de que termine el otro
                ('end_date', '>=', record.event_id.start_date),  # El evento termina depués de que empiece el otro
                #('id', 'in', record.event_ids.employee_light_ids.ids),
            ])
            
            if conflicting_events:
                conflicting_event_names = []
                for event in conflicting_events:
                    if event.id != record.event_id.id:
                        if self.employee_id in event.employee_light_ids.employee_id:
                            conflicting_event_names.append(event.name)
                
                record.conflicting_event_info = ', '.join(conflicting_event_names)

                #conflicting_event_names = ', '.join(conflicting_events.mapped('name'))
                #record.conflicting_event_info = conflicting_event_names
            else:
                record.conflicting_event_info = ''