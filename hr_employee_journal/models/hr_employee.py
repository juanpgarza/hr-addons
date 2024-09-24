# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

import logging

from ast import literal_eval
from odoo import fields, models, _, api
from odoo.exceptions import UserError
from odoo.fields import Datetime
from datetime import date, datetime
import pytz

_logger = logging.getLogger(__name__)

class HrEmployee(models.Model):
    _inherit = 'hr.employee'

    @api.model
    def _generate_journal_entries(self,employee_id,start_dt,end_dt):
        
        # if employee_id:
        #     employees = employee_id
        # else:
        #     employees = self.env['hr.employee'].search([])

        # for rec in employees:

        start_dt = fields.Date.from_string(start_dt)
        end_dt = fields.Date.from_string(end_dt)
        
        user_tz = pytz.timezone(self.env.user.tz)
        start_dt = datetime(2024, 8, 1, tzinfo=user_tz)
        end_dt = datetime(2024, 8, 31, tzinfo=user_tz)        
        current_calendar_id = employee_id.with_context(date=start_dt.date()).current_calendar_id

        # calendar = employee_sl.resource_id.calendar_id.with_context(
        #     exclude_public_holidays=True
        # )

        print(employee_id.resource_calendar_id.name)
        attendance_intervals = employee_id.resource_calendar_id.with_context(exclude_public_holidays=True)._attendance_intervals_batch(start_dt,end_dt,employee_id.resource_id)
        # expected_attendances = employee_id._get_expected_attendances(start_dt,end_dt)
        # import pdb; pdb.set_trace()
        # attendance_intervals[0]._items --> te da los dias y horarios que debería trabajar segun el calendario teniendo en cuenta
        # los dias festivos y las ausencias (?)
        # attendance_intervals[employee_id.resource_id]._items[0]
        for ai in attendance_intervals[employee_id.resource_id.id]._items:
            # import pdb; pdb.set_trace()
            print(ai[0].date())
            journal_entry_id = self.env['hr.journal.entry'].create_journal_entry(employee_id,ai[0].date())
            self.env['hr.attendance'].update_journal_entry(journal_entry_id)

        return attendance_intervals
    
    @api.model
    def probar(self, employee = 1):
        # self.env['hr.employee'].probar(17)
        employee_id = self.env['hr.employee'].browse(employee)
        print(employee_id.name)
        self.env['hr.employee']._generate_journal_entries(employee_id,'2024-09-01','2024-09-30')