from odoo import fields, models, api
import datetime


class TimesheetSettings(models.Model):
    _inherit = 'hr.employee'

    daily_hours = fields.Float(string='Daily Hours', compute="logged_hours_in_current_day")
    max_daily_hours = fields.Integer(string='Hours/day', required=True)
    weekly_hours = fields.Float(string='Weekly Hours', compute="logged_hours_in_current_week")
    max_weekly_hours = fields.Integer(string='Hours/week', required=True)
    monthly_hours = fields.Float(string='Monthly Hours', compute="logged_hours_in_current_month")
    max_monthly_hours = fields.Integer(string='Hours/month', required=True)
    automatic_email = fields.Boolean(string='Automatic email', default=False)
    specific_project = fields.Many2many('project.project', string='Specific Project')

    def logged_hours_in_current_day(self):
        for recordset in self:
            daily_hours = 0
            if self.user_id:
                today = datetime.datetime.today()
                starting_hour_of_day = datetime.datetime.combine(today, datetime.datetime.min.time())
                ending_hour_of_day = datetime.datetime.combine(today, datetime.datetime.max.time())
                analytic_ids = self.env['account.analytic.line'].search(
                    [('user_id', '=', recordset.user_id.id), ('date', '>=', starting_hour_of_day),
                     ('date', '<=', ending_hour_of_day)])
                if analytic_ids:
                    for line in analytic_ids:
                        daily_hours = line.unit_amount + daily_hours
                        self.daily_hours = daily_hours
                    else:
                        self.daily_hours = daily_hours
                else:
                    self.daily_hours = daily_hours

    def logged_hours_in_current_week(self):
        for recordset in self:
            weekly_hours = 0
            if self.user_id:
                today = datetime.datetime.today()
                starting_date_of_week = today - datetime.timedelta(days=today.weekday())
                ending_date_of_week = starting_date_of_week + datetime.timedelta(days=today.weekday())
                analytic_ids = self.env['account.analytic.line'].search(
                    [('user_id', '=', recordset.user_id.id), ('date', '>=', starting_date_of_week),
                     ('date', '<=', ending_date_of_week)])
                if analytic_ids:
                    for line in analytic_ids:
                        weekly_hours = line.unit_amount + weekly_hours
                        self.weekly_hours = weekly_hours
                    else:
                        self.weekly_hours = weekly_hours
                else:
                    self.weekly_hours = weekly_hours

    def logged_hours_in_current_month(self):
        for recordset in self:
            monthly_hours = 0
            if self.user_id:
                todayDate = datetime.datetime.today()
                starting_date_of_month = todayDate.replace(day=1)
                ending_date_of_month = starting_date_of_month + datetime.timedelta(days=todayDate.day - 1)
                analytic_ids = self.env['account.analytic.line'].search(
                    [('user_id', '=', recordset.user_id.id), ('date', '>=', starting_date_of_month),
                     ('date', '<=', ending_date_of_month)])
                if analytic_ids:
                    for line in analytic_ids:
                        monthly_hours = line.unit_amount + monthly_hours
                        self.monthly_hours = monthly_hours
                else:
                    self.monthly_hours = monthly_hours
            else:
                self.monthly_hours = monthly_hours

    def action_send_mail(self):
        print('send email')
        # action_url = '%s/web#menu_id=%s&action=%s' % (
        #     self.env['ir.config_parameter'].sudo().get_param('web.base.url'),
        #     self.env.ref('hr_timesheet.timesheet_menu_root').id,
        #     self.env.ref(action_xmlid).id,
        # )
        template_id = self.env.ref('timesheets_by_employee.mail_template_reminder_user').id
        template = self.env['mail.template'].browse(template_id)

        # template_ctx = {'action_url': action_url}
        # if additionnal_values:
        #     template_ctx.update(additionnal_values)
        template.send_mail(self.id, force_send=True)

    def _cron_timesheet_reminder_employee(self):

        employees = self.env['hr_employee'].search([('automatic_email', '=', True)])
        employees.send_mail()
