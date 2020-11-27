# -*- coding: utf-8 -*-
# from odoo import http


# class TimesheetsByEmployee(http.Controller):
#     @http.route('/timesheets_by_employee/timesheets_by_employee/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/timesheets_by_employee/timesheets_by_employee/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('timesheets_by_employee.listing', {
#             'root': '/timesheets_by_employee/timesheets_by_employee',
#             'objects': http.request.env['timesheets_by_employee.timesheets_by_employee'].search([]),
#         })

#     @http.route('/timesheets_by_employee/timesheets_by_employee/objects/<model("timesheets_by_employee.timesheets_by_employee"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('timesheets_by_employee.object', {
#             'object': obj
#         })
