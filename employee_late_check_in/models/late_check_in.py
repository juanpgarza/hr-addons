# -*- coding: utf-8 -*-
from odoo import models, fields, api


class LateCheckIn(models.Model):
    _name = 'late.check_in'
    _description = 'Llegadas Tarde'

    name = fields.Char(string="Nombre")
    employee_id = fields.Many2one('hr.employee', string="Empleado")
    late_minutes = fields.Integer(string="Minutos tarde")
    date = fields.Date(string="Fecha")
    state = fields.Selection([('draft', 'Borrador'),
                              ('approved', 'Aprobado'),
                              ('refused', 'Rechazado')], string="Estado",
                             default="draft")
    attendance_id = fields.Many2one('hr.attendance', string='Asistencia')

    # current_user_boolean = fields.Boolean()
    @api.model
    def create(self, values):
        seq = self.env['ir.sequence'].next_by_code('late.check_in') or '/'
        values['name'] = seq
        return super(LateCheckIn, self.sudo()).create(values)

    def approve(self):
        self.state = 'approved'

    def reject(self):
        self.state = 'refused'
