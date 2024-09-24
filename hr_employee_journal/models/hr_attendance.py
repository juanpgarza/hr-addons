from odoo import models, api
from datetime import date, datetime

class HrAttendance(models.Model):
    _inherit = 'hr.attendance'

    def write(self, vals):
        res = super().write(vals)
        # fields_to_check = {'number_of_days', 'date_from', 'date_to', 'state', 'employee_id', 'holiday_status_id'}
        # fields_to_check = {'number_of_days', 'date_from', 'date_to', 'state', 'employee_id', 'holiday_status_id'}
        # if not any(field for field in fields_to_check if field in vals):
        #     return res
        #User may not have access to overtime_id field
        for rec in self.sudo():
            # si no existe una entrada, la crea
            hr_journal_id = self.env['hr.journal.entry'].create_journal_entry(rec.employee_id,rec.check_in)
            # import pdb; pdb.set_trace()
            hr_journal_id.attendance_id = self.id
        
        return res

    @api.model    
    def update_journal_entry(self, hr_journal_id):
        # busco la fichada con fecha de ingreso hr_journal_id.date
        # y asigno esa fichada a la journal entry
        # hr_attendance_id = self.env['hr.attendance'].search([
        #                     ('employee_id', '=', hr_journal_id.employee_id.id),
        #                     ('check_in', '=', hr_journal_id.date),
        #                 ], limit=1)
        Attendance = self.env['hr.attendance'].search([('employee_id', '=', hr_journal_id.employee_id.id)])
        hr_attendance_id = Attendance.filtered(lambda x: x.check_in.date() == hr_journal_id.date)
        # import pdb; pdb.set_trace()
        if hr_attendance_id:
            hr_journal_id.attendance_id = hr_attendance_id
        else:
            return False