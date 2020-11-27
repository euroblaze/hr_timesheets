from odoo import models, fields


class EmployeeTimesheet(models.TransientModel):
    _name = 'timesheet.wizard'

    employee = fields.Many2one('hr.employee', string="Employee", readonly=True)
    project = fields.Many2one('project.project', string='Project')
    from_date = fields.Date(string="Starting Date")
    to_date = fields.Date(string="Ending Date")

    # def write(self):
    #     values = {
    #         'from_date': self.from_date,
    #         'to_date': self.to_date,
    #         'employee': self.employee.id,
    #         'project': self.project.id
    #
    #     }
    #     return super(EmployeeTimesheet, self).write(values)

    def print_timesheet(self):
        # Redirects to the report with the values obtained from the wizard
        # 'data['form']': name of employee,the date duration and project
        data = {
            'start_date': self.from_date,
            'end_date': self.to_date,
            'employee': self.employee.id,
            'project': self.project.id
        }
        return self.env.ref('timesheets_by_employee.action_report_print_timesheets').report_action(self, data=data)
