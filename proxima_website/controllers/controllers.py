# -*- coding: utf-8 -*-
# from odoo import http


# class ProximaWebsite(http.Controller):
#     @http.route('/proxima_website/proxima_website/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/proxima_website/proxima_website/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('proxima_website.listing', {
#             'root': '/proxima_website/proxima_website',
#             'objects': http.request.env['proxima_website.proxima_website'].search([]),
#         })

#     @http.route('/proxima_website/proxima_website/objects/<model("proxima_website.proxima_website"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('proxima_website.object', {
#             'object': obj
#         })
