# -*- coding: utf-8 -*-
###################################################################################

from datetime import datetime, timedelta, date
from pytz import timezone, UTC
import pytz
from odoo import models, fields, api


class HrAttendance(models.Model):
    _inherit = 'hr.attendance'

    late_check_in = fields.Integer(string="Llegada Tarde (Minutos)", compute="get_late_minutes")

    def get_late_minutes(self):
        for rec in self:

            rec.late_check_in = 0.0
            week_day = rec.sudo().check_in.weekday()
            # if rec.employee_id.contract_id:
            # modificacion para que no dependa del contrato
            # todo: elegir el calendario que corresponda para la fecha (módulo de OCA con histórico de calendario para el empleado)
            # if rec.id == 480:
            # import pdb; pdb.set_trace()
            work_schedule = rec.sudo().employee_id.with_context(date=rec.check_in.date()).resource_calendar_id
            for schedule in work_schedule.sudo().attendance_ids:
                if schedule.dayofweek == str(week_day) and schedule.day_period == 'morning':
                    work_from = schedule.hour_from
                    result = '{0:02.0f}:{1:02.0f}'.format(*divmod(work_from * 60, 60))

                    # Cuidado: el que ejecuta esto es el OdooBot, tiene que estar OK el tz del OdooBot
                    user_tz = self.env.user.tz
                    dt = rec.check_in

                    if user_tz in pytz.all_timezones:
                        old_tz = pytz.timezone('UTC')
                        new_tz = pytz.timezone(user_tz)
                        dt = old_tz.localize(dt).astimezone(new_tz)
                    str_time = dt.strftime("%H:%M")
                    check_in_date = datetime.strptime(str_time, "%H:%M").time()
                    start_date = datetime.strptime(result, "%H:%M").time()
                    t1 = timedelta(hours=check_in_date.hour, minutes=check_in_date.minute)
                    t2 = timedelta(hours=start_date.hour, minutes=start_date.minute)
                    # if rec.id == 480:
                    #     import pdb; pdb.set_trace()
                    if check_in_date > start_date:
                        final = t1 - t2
                        rec.sudo().late_check_in = final.total_seconds() / 60

    def late_check_in_records(self):
        existing_records = self.env['late.check_in'].sudo().search([]).attendance_id.ids
        # minutes_after: creo que es la tolerancia antes de considerarlo llegada tarde
        minutes_after = int(self.env['ir.config_parameter'].sudo().get_param('late_check_in_after')) or 0
        # max_limit: creo que es el límite máximo para considerarlo como llegada tarde --> CUIDADO: le pongo 60 (120 no me funcionó, me tomaba 5!)
        max_limit = int(self.env['ir.config_parameter'].sudo().get_param('maximum_minutes')) or 0
        late_check_in_ids = self.sudo().search([('id', 'not in', existing_records)])
        for rec in late_check_in_ids:
            # no entiendo porque le suma 210 minutos. Sin esto funciona OK
            # late_check_in = rec.sudo().late_check_in + 210
            late_check_in = rec.sudo().late_check_in
            # if rec.id == 480:
            #     import pdb; pdb.set_trace()
            if rec.late_check_in > minutes_after and late_check_in > minutes_after and late_check_in < max_limit:
                self.env['late.check_in'].sudo().create({
                    'employee_id': rec.employee_id.id,
                    'late_minutes': late_check_in,
                    'date': rec.check_in.date(),
                    'attendance_id': rec.id,
                })
