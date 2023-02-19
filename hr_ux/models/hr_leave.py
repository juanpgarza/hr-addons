# Copyright 2021 juanpgarza - Juan Pablo Garza <juanp@juanpgarza.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models, _
from datetime import datetime, timedelta
from odoo.tools.float_utils import float_round

class HrLeave(models.Model):
    _inherit = 'hr.leave'

    def _calculate_days(self,date_from,date_to):
        if date_to and date_from:
            delta = date_to - date_from
            return delta.days + 1

    @api.depends('date_from', 'date_to', 'employee_id')
    def _compute_number_of_days(self):
        res = super(HrLeave,self)._compute_number_of_days()
        for rec in self:            
            # import pdb; pdb.set_trace()
            if rec.holiday_status_id.request_unit == 'day':
                if rec.date_to and rec.date_from:                    
                    rec.number_of_days = rec._calculate_days(rec.date_from,rec.date_to)
                        
        return res

    @api.depends('number_of_hours_display', 'number_of_days_display')
    def _compute_duration_display(self):
        for rec in self:
            super(HrLeave,self)._compute_duration_display()
            if rec.holiday_status_id.request_unit == 'day':
                rec.duration_display = '%g %s' % ((float_round(rec.number_of_days, precision_digits=2)),_('day(s)'))
