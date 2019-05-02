# -*- coding: utf-8 -*-
from odoo import http

# class Dm1(http.Controller):
#     @http.route('/dm1/dm1/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/dm1/dm1/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('dm1.listing', {
#             'root': '/dm1/dm1',
#             'objects': http.request.env['dm1.dm1'].search([]),
#         })

#     @http.route('/dm1/dm1/objects/<model("dm1.dm1"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('dm1.object', {
#             'object': obj
#         })