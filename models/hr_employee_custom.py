# -*- coding: utf-8 -*-

from odoo import models, fields, api

class HREployeeCustom(models.Model):
    _name="gestion_eventos.hr_employee_custom"
    _description="Empleado heredado"

    _inherit="hr.employee"

    category_ids = fields.Many2many('hr.employee.category', relation="gestion_eventos_employee_category_rel")