# -*- coding: utf-8 -*-
# from odoo import http


# class CustomMailing(http.Controller):
#     @http.route('/custom_mailing/custom_mailing', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/custom_mailing/custom_mailing/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('custom_mailing.listing', {
#             'root': '/custom_mailing/custom_mailing',
#             'objects': http.request.env['custom_mailing.custom_mailing'].search([]),
#         })

#     @http.route('/custom_mailing/custom_mailing/objects/<model("custom_mailing.custom_mailing"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('custom_mailing.object', {
#             'object': obj
#         })
