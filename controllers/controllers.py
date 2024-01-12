# -*- coding: utf-8 -*-
# from odoo import http


# class GestionEventos(http.Controller):
#     @http.route('/gestion_eventos/gestion_eventos/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/gestion_eventos/gestion_eventos/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('gestion_eventos.listing', {
#             'root': '/gestion_eventos/gestion_eventos',
#             'objects': http.request.env['gestion_eventos.gestion_eventos'].search([]),
#         })

#     @http.route('/gestion_eventos/gestion_eventos/objects/<model("gestion_eventos.gestion_eventos"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('gestion_eventos.object', {
#             'object': obj
#         })
