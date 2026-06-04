# -*- coding: utf-8 -*-
# from odoo import http


# class HrContractFootball(http.Controller):
#     @http.route('/hr_contract_football/hr_contract_football', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hr_contract_football/hr_contract_football/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('hr_contract_football.listing', {
#             'root': '/hr_contract_football/hr_contract_football',
#             'objects': http.request.env['hr_contract_football.hr_contract_football'].search([]),
#         })

#     @http.route('/hr_contract_football/hr_contract_football/objects/<model("hr_contract_football.hr_contract_football"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hr_contract_football.object', {
#             'object': obj
#         })

