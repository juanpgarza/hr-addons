from odoo import models


class HRLeave(models.Model):
    _inherit = 'hr.leave'

    # @api.model_create_multi
    # def create(self, vals_list):
    #     res = super().create(vals_list)
    #     self._check_overtime_deductible(res)
    #     return res

    def write(self, vals):
        res = super().write(vals)
        # fields_to_check = {'number_of_days', 'date_from', 'date_to', 'state', 'employee_id', 'holiday_status_id'}
        # fields_to_check = {'number_of_days', 'date_from', 'date_to', 'state', 'employee_id', 'holiday_status_id'}
        # if not any(field for field in fields_to_check if field in vals):
        #     return res
        #User may not have access to overtime_id field
        for rec in self.sudo():
            # 
            vals = {
                'employee_id': rec.employee_id.id,
                'date': rec.date_from,                
            }            
            # si no existe una entrada, la crea
            hr_journal_id = self.env['hr.journal.entry'].create_journal_entry(rec.employee_id,rec.date_from)
            # import pdb; pdb.set_trace()
            hr_journal_id.leave_id = self.id
        
        return res

