# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class HrEmployee(models.Model):
    _inherit = 'hr.employee'

    late_check_in_count = fields.Integer(string="Late Check-In", compute="get_late_check_in_count")

    # Campo computado para obtener el calendario basado en la fecha del contexto
    current_calendar_id = fields.Many2one(
        'resource.calendar', 
        string='Calendario Actual', 
        compute='_compute_current_calendar',
        store=False
    )

    @api.depends_context('date')
    def _compute_current_calendar(self):
        """Computa el calendario basado en la fecha pasada en el contexto."""
        for employee in self:
            # Obtener la fecha del contexto
            date_str = self.env.context.get('date')
            
            # import pdb; pdb.set_trace()

            # self.env['hr.employee'].with_context(date='2024-09-05').browse(17).current_calendar_id.name
            if date_str:
                date = fields.Date.from_string(date_str) if isinstance(date_str, str) else date_str

                # Buscar el calendario relevante en la base de datos considerando que date_end puede ser False
                relevant_calendars = self.env['hr.employee.calendar'].search([
                    ('employee_id', '=', employee.id),
                    ('date_start', '<=', date),
                    '|',  # OR lógico en Odoo
                    ('date_end', '>=', date),
                    ('date_end', '=', False)
                ], limit=1)

                # Asignar el calendario actual si existe
                employee.current_calendar_id = relevant_calendars[0].calendar_id if relevant_calendars else False
            else:
                employee.current_calendar_id = False

    def action_to_open_late_check_in_records(self):
        domain = [
            ('employee_id', '=', self.id),
        ]
        return {
            'name': _('Employee Late Check-in'),
            'domain': domain,
            'res_model': 'late.check_in',
            'type': 'ir.actions.act_window',
            'view_mode': 'tree,form',
            'limit': 80,
        }

    def get_late_check_in_count(self):
        self.late_check_in_count = self.env['late.check_in'].search_count([('employee_id', '=', self.id)])


class HrEmployees(models.Model):
    _inherit = 'hr.employee.public'

    late_check_in_count = fields.Integer(string="Late Check-In", compute="get_late_check_in_count")

    def action_to_open_late_check_in_records(self):
        domain = [
            ('employee_id', '=', self.id),
        ]
        return {
            'name': _('Employee Late Check-in'),
            'domain': domain,
            'res_model': 'late.check_in',
            'type': 'ir.actions.act_window',
            'view_mode': 'tree,form',
            'limit': 80,
        }

    def get_late_check_in_count(self):
        self.late_check_in_count = self.env['late.check_in'].search_count([('employee_id', '=', self.id)])
