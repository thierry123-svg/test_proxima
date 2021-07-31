# -*- coding: utf-8 -*-
from odoo import http

# class SaleQuote(http.Controller):
#     @http.route('/sale_quote/sale_quote/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/sale_quote/sale_quote/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('sale_quote.listing', {
#             'root': '/sale_quote/sale_quote',
#             'objects': http.request.env['sale_quote.sale_quote'].search([]),
#         })

#     @http.route('/sale_quote/sale_quote/objects/<model("sale_quote.sale_quote"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('sale_quote.object', {
#             'object': obj
#         })