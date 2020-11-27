from odoo import models, api


class ReportTimesheet(models.AbstractModel):
    _name = 'report.timesheets_by_employee.report_timesheets'

    # input : name of employe ,the starting date and ending date and project
    # output: timesheets by that particular employee within that period and the total duration

    def get_timesheets(self, data):

        if data['start_date'] and data['end_date']:
            rec = self.env['account.analytic.line'].search([('employee_id', '=', data['employee']),
                                                            ('date', '>=', data['start_date']),
                                                            ('date', '<=', data['end_date']),
                                                            ])
        elif data['start_date']:
            rec = self.env['account.analytic.line'].search([('employee_id', '=', data['employee']),
                                                            ('date', '>=', data['start_date'])])
        elif data['end_date']:
            rec = self.env['account.analytic.line'].search([('employee_id', '=', data['employee']),
                                                            ('date', '<=', data['end_date'])])
        else:
            rec = self.env['account.analytic.line'].search([('employee_id', '=', data['employee'])])
        records = []
        total = 0
        # put all timesheets in records
        for r in rec:
            vals = {'project': r.project_id.id,
                    'user': r.employee_id.name,
                    'duration': r.unit_amount,
                    'date': r.date,
                    }

            # if timesheet is from the selected project, add it

            if not data['project'] or (data['project'] and r.project_id.id == data['project']):

                total += r.unit_amount
                records.append(vals)

        return [records, total]

    @api.model
    def _get_report_values(self, docids, data=None):

        # we are overwriting this function because we need to show values from other models in the report

        o = data
        # data = self.env['timesheet.wizard'].browse(self.env.context.get('active_id'))
        # identification = []
        # for i in self.env['hr.employee'].search([('id', '=', data['employee'])]):
        #     if i:
        #         identification.append({'id': i.id, 'name': i.name})
        timesheets = self.get_timesheets(data)
        employee = self.env['hr.employee'].browse(data['employee'])
        company_name = employee.company_id
        period = None
        if data['start_date'] and data['end_date']:
            period = "From " + data['start_date'] + " To " + data['end_date']
        elif data['start_date']:
            period = "From " + data['start_date']
        elif data['start_date']:
            period = " To " + data['end_date']

        return {
            'doc_ids': self.ids,
            'docs': data,
            'timesheets': timesheets[0],
            'total': timesheets[1],
            'company': company_name,
            'employee': employee,
            'period': period,
        }
