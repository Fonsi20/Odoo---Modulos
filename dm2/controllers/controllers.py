# -*- coding: utf-8 -*-
from odoo import http

# class Dm2(http.Controller):
#     @http.route('/dm2/dm2/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/dm2/dm2/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('dm2.listing', {
#             'root': '/dm2/dm2',
#             'objects': http.request.env['dm2.dm2'].search([]),
#         })

#     @http.route('/dm2/dm2/objects/<model("dm2.dm2"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('dm2.object', {
#             'object': obj
#         })