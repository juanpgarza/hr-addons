# -*- coding: utf-8 -*-

from odoo import models, fields


class LateCheckinSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    # deduction_amount = fields.Float(string="Deduction Amount",
    #                                 config_parameter='employee_late_check_in.deduction_amount')
    maximum_minutes = fields.Char(string="Máximo tolerable para ser computado como llegada tarde:",
                                  config_parameter='employee_late_check_in.maximum_minutes')
    late_check_in_after = fields.Char(string="Se considera llegada tarde a partir de:",
                                      config_parameter='employee_late_check_in.late_check_in_after')
    # unpaid_leave = fields.Boolean(string="Unpaid Leave",
    #                                   config_parameter='employee_late_check_in.unpaid_leave')
    # deduction_type = fields.Selection([('minutes', 'Per Minutes'), ('total', 'Per Total')],
    #                               config_parameter='employee_late_check_in.deduction_type', default="minutes")

    def set_values(self):
        res = super(LateCheckinSettings, self).set_values()
        # self.env['ir.config_parameter'].sudo().set_param('deduction_amount', self.deduction_amount)
        self.env['ir.config_parameter'].sudo().set_param('maximum_minutes', self.maximum_minutes)
        self.env['ir.config_parameter'].sudo().set_param('late_check_in_after', self.late_check_in_after)
        # self.env['ir.config_parameter'].sudo().set_param('unpaid_leave', self.unpaid_leave)
        # self.env['ir.config_parameter'].sudo().set_param('deduction_type', self.deduction_type)
        return res
