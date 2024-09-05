# -*- coding: utf-8 -*-

{
    'name': 'Employee Late Check-in',
    'version': '15.0.1.0.0',
    'summary': """This module Allows Employee Late check-in deduction/penalty""",
    'description': """This module Allows Employee Late check-in deduction/penalty""",
    'author': "Cybrosys Techno Solutions",
    'company': 'Cybrosys Techno Solutions',
    'website': 'https://www.cybrosys.com',
    'maintainer': 'Cybrosys Techno Solutions',
    'category': 'Human Resources',
    'depends': ['hr_attendance', 'hr_employee_calendar_planning'],
    'data': [
        'views/res_config_settings.xml',
        'views/hr_attendance_view.xml',
        'views/late_check_in_view.xml',
        'views/hr_employee.xml',
        'security/ir.model.access.csv',
        'data/cron.xml',
    ],
    'images': ['static/description/banner.png'],
    'license': 'AGPL-3',
    'installable': True,
    'auto_install': False,
    'application': False,
}
