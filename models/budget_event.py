# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Budget_Event(models.Model):
    _name = 'gestion_eventos.budget_event'
    _description = 'Budget_Event'

    # Herencia
    _inherit = 'gestion_eventos.budget_abstract'

    template_id = fields.Many2one('gestion_eventos.budget_template', string='Plantilla de presupuesto')
    line_ids = fields.One2many('gestion_eventos.line', 'budget_event_id', string='Líneas')

    @api.onchange('template_id')
    def _onchange_template_id(self):
        if len(self.line_ids) > 0 :
            return {"warning":{"title":"Atención!!!", "message":"Lo siento pero tienes lineas metidas"}}
        if self.template_id:
            # Limpiamos las líneas actuales
            self.clean_lines()
            
            # Creamos nuevas instancias de las líneas basadas en las del template
            new_lines = []
            for line in self.template_id.line_ids:
                new_line = self.env['gestion_eventos.line'].create({
                    'code': line.code,
                    'concept_id': line.concept_id.id,
                    'quantity': line.quantity,
                    # Asegúrate de establecer otros campos relevantes aquí
                })
                new_lines.append(new_line.id)
            
            # Agregamos las nuevas líneas al budget_event
            self.write({'line_ids': [(6, 0, new_lines)]})
    
    def clean_lines(self):
        self.line_ids.unlink()

    @api.onchange('line_ids')
    def _onchange_line_ids(self):
        for i, line in enumerate(self.line_ids, start=1):
            line.code = i

    """
    def write(self, vals):
        for index, line in vals["line_ids"]:
            line.code = index+1
        super(Budget_Event,self).write(vals)
    """  
