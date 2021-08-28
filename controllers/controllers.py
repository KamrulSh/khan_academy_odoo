# -*- coding: utf-8 -*-
# from odoo import http


# class KhanAcademy(http.Controller):
#     @http.route('/khan_academy/khan_academy/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/khan_academy/khan_academy/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('khan_academy.listing', {
#             'root': '/khan_academy/khan_academy',
#             'objects': http.request.env['khan_academy.khan_academy'].search([]),
#         })

#     @http.route('/khan_academy/khan_academy/objects/<model("khan_academy.khan_academy"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('khan_academy.object', {
#             'object': obj
#         })
