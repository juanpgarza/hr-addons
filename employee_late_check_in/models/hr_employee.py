# -*- coding: utf-8 -*-

from odoo import models, fields, _


class HrEmployee(models.Model):
    _inherit = 'hr.employee'

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
