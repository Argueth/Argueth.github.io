# -*- coding: utf-8 -*-

from odoo import models, fields, api

class SoundEmployeeEventRel(models.Model):
    _name="gestion_eventos.sound_employee_event_rel"
    _description="Empleados de iluminación"

    employee_id = fields.Many2one('hr.employee', required=True)
    event_id = fields.Many2one('gestion_eventos.event', required=True)

    employee_name = fields.Char(string="Nombre", related='employee_id.name')
    department_id = fields.Many2one('hr.department', string="Departamento", related='employee_id.department_id')
    department_name = fields.Char(string='Nombre del departmento', related='department_id.name')
    conflicting_event_info = fields.Char(string="Evento en conflicto", compute='_compute_conflicting_event_info')

    _sql_constraints = [
        ('unique_combination','unique(employee_id,event_id)','Employee plus event combination must be unique.')
    ]

    @api.depends('employee_id', 'event_id')
    def _compute_conflicting_event_info(self):
        for record in self:
            conflicting_events = self.env['gestion_eventos.event'].search([
                '|',
                '&', ('start_date', '<=', record.event_id.start_date), ('end_date', '>=', record.event_id.start_date),
                '&', ('start_date', '<=', record.event_id.end_date), ('end_date', '>=', record.event_id.end_date)
            ])
            
            if conflicting_events:
                conflicting_event_names = []
                for event in conflicting_events:
                    if event.id != record.event_id.id:
                        if record.employee_id in event.employee_light_ids.employee_id or record.employee_id in event.employee_sound_ids.employee_id or record.employee_id in event.employee_mount_ids.employee_id:
                            conflicting_event_names.append(event.name)
                
                record.conflicting_event_info = ', '.join(conflicting_event_names)

            else:
                record.conflicting_event_info = ''
    
    def write(self, vals):
        super(SoundEmployeeEventRel, self).write(vals)