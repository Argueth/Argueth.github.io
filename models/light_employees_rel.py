# -*- coding: utf-8 -*-

from odoo import models, fields, api

class LightEmployeesRel(models.Model):
    _name="gestion_eventos.light_employees_rel"
    _description="Empleados de iluminación"

    employee = fields.Many2one('hr.employee')
    event = fields.Many2one('gestion_eventos.event')

    _sql_constraints = [
        ('unique_combination','unique(employee,event)','Employee plus event combination must be unique.')
    ]