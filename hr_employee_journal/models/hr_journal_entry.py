from odoo import models, fields, api
from odoo.exceptions import ValidationError

class HrJournalEntry(models.Model):
    _name = 'hr.journal.entry'
    _description = 'Novedad diaria'
    # _rec_name = 'journal_id'
    _inherit = ["mail.thread", "mail.activity.mixin"]
    # _order = 'id'

    name = fields.Char()
    employee_id = fields.Many2one('hr.employee', string="Employee")
    # late_minutes = fields.Integer(string="Late Minutes")
    date = fields.Date(string="Date")

    # leave_id = fields.Many2one('hr.leave', string='Ausencia', compute='_compute_leave', store=True,)
    leave_id = fields.Many2one('hr.leave', string='Ausencia')
    leave_state = fields.Selection(related='leave_id.state')

    attendance_id = fields.Many2one('hr.attendance', string='Asistencia')
    check_in = fields.Datetime(related='attendance_id.check_in')
    check_out = fields.Datetime(related='attendance_id.check_out')
    worked_hours = fields.Float(related='attendance_id.worked_hours')

    late_check_in_id = fields.Many2one('late.check_in', string='Llegada tarde')
    late_minutes = fields.Integer(related='late_check_in_id.late_minutes')

    note = fields.Html("Notas")

    @api.model
    def create_journal_entry(self, employee_id, date):
        # si ya existe solo devuelve el ID

        # employee = self.env['hr.employee'].browse(1)
        # self.env['hr.journal.entry'].create_journal_entry(employee,'2024-09-23')

        journal_entry_id = self.env['hr.journal.entry'].search([
            ('employee_id', '=', employee_id.id),
            ('date', '=', date),
        ], limit=1)

        if not journal_entry_id:
            vals = {
                'employee_id': employee_id.id,
                'date': date,
            }

            journal_entry_id = self.env['hr.journal.entry'].create(vals)
            
        return journal_entry_id
    
    # @api.depends('payment_id.amount', 'move_id.amount_total')
    # def _compute_leave(self):
        
    #     for rec in self:
    #         leave_id = self.env['hr.leave'].search([
    #             ('employee_id', '=', rec.employee_id.id),
    #             ('date_from', '>=', rec.date),
    #             ('date_to', '<=', rec.date),
    #         ], limit=1)
