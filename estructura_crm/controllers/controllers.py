# -*- coding: utf-8 -*-
from odoo import http

# class EstructuraCrm(http.Controller):
#     @http.route('/estructura_crm/estructura_crm/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/estructura_crm/estructura_crm/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('estructura_crm.listing', {
#             'root': '/estructura_crm/estructura_crm',
#             'objects': http.request.env['estructura_crm.estructura_crm'].search([]),
#         })

#     @http.route('/estructura_crm/estructura_crm/objects/<model("estructura_crm.estructura_crm"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('estructura_crm.object', {
#             'object': obj
#         })