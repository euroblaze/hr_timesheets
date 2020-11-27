# -*- coding: utf-8 -*-
{
    'name': "HR timesheets",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'hr', 'hr_timesheet', 'hr_attendance', 'hr_timesheet_attendance'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/employee_view.xml',
        'views/report.xml',
        'views/report_timesheets.xml',
        'views/timesheet_wizard.xml',
        'views/timesheets_settings.xml',
        'views/cron.xml',
        'views/mail_template.xml',


    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
