from odoo import models, fields, api
from odoo.exceptions import ValidationError

class HrJournalEntry(models.Model):
    _name = 'hr.journal.entry'
    _description = 'Novedad diaria'
    # _rec_name = 'journal_id'
    _inherit = ["mail.thread", "mail.activity.mixin"]
    # _order = 'id'


# _attendance_intervals_batch