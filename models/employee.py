from odoo import fields, models


class Employee(models.Model):
    _inherit = 'hr.employee'

    def billing_report(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Billing Report',
            'view_mode': 'form',
            'res_model': 'timesheet.wizard',
            'target': 'new',
            'context': {

                'default_employee': self.id,

            }
        }
