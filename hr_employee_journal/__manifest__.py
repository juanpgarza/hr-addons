# Copyright 2021 juanpgarza - Juan Pablo Garza <juanp@juanpgarza.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "hr_employee_journal",
    "summary": "",
    "version": "15.0.1.0.0",
    "category": "Human Resources",
    "website": "https://github.com/juanpgarza/hr-addons",
    "author": "juanpgarza",
    "license": "AGPL-3",
    "depends": [
                "hr",
                "hr_attendance",
                "hr_holidays",
                "hr_holidays_attendance",
                # "hr_presence",
                "employee_late_check_in",
                "hr_holidays_public",
            ],
    "data": [     
        'security/ir.model.access.csv',
        'views/hr_journal_entry_views.xml',
        ],
    "installable": True,
}
