# -*- coding: utf-8 -*-
# from odoo import http


# class PartnerLedgProdRpt(http.Controller):
#     @http.route('/partner_ledg_prod_rpt/partner_ledg_prod_rpt', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/partner_ledg_prod_rpt/partner_ledg_prod_rpt/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('partner_ledg_prod_rpt.listing', {
#             'root': '/partner_ledg_prod_rpt/partner_ledg_prod_rpt',
#             'objects': http.request.env['partner_ledg_prod_rpt.partner_ledg_prod_rpt'].search([]),
#         })

#     @http.route('/partner_ledg_prod_rpt/partner_ledg_prod_rpt/objects/<model("partner_ledg_prod_rpt.partner_ledg_prod_rpt"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('partner_ledg_prod_rpt.object', {
#             'object': obj
#         })
