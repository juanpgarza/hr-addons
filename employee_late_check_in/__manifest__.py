# -*- coding: utf-8 -*-

{
    "name": "Llegada tarde de empleados",
    "summary": "",
    "version": "15.0.1.0.0",
    "category": "Human Resources",
    "website": "https://github.com/juanpgarza/hr-addons",
    "author": "juanpgarza",
    "license": "AGPL-3",
    'depends': [
            'hr_attendance', 
            # 'hr_employee_calendar_planning' # https://github.com/OCA/hr
            ],
    'data': [
        'views/res_config_settings.xml',
        'views/hr_attendance_view.xml',
        'views/late_check_in_view.xml',
        'views/hr_employee.xml',
        'security/ir.model.access.csv',
        'data/cron.xml',
    ],
    'license': 'AGPL-3',
    'installable': False,
    'auto_install': False,
    'application': False,
}
