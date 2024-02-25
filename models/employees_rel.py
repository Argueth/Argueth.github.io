# -*- coding: utf-8 -*-

from odoo import models, fields, api

class EmployeesRel(models.Model):
    _name="gestion_eventos.employees_rel"
    _description="Empleados de iluminación"

    employee_ids = fields.Many2one('hr.employee')
    event_ids = fields.Many2one('gestion_eventos.event')

    employee_name = fields.Char(string="Nombre", related='employee_ids.name')
    department_id = fields.Many2one('hr.department', string="Departamento", related='employee_ids.department_id')

    _sql_constraints = [
        ('unique_combination','unique(employee,event)','Employee plus event combination must be unique.')
    ]