import pytz
from odoo import models, api, fields, _
import datetime
from dateutil import tz


class Employee(models.Model):
    _inherit = "hr.employee"

    overt_time = fields.Boolean(string="OverTime Permit")
    def covert_time_to_user_tz(self, stddatetime):
            user_tz = tz.gettz(self.env.user.tz)
            std_tz = tz.gettz('UTC')
            userdatetime = stddatetime.replace(tzinfo=std_tz).astimezone(user_tz).replace(tzinfo=None)
            return userdatetime
    def covert_time_to_std_tz(self, stddatetime):
        user_tz = tz.gettz(self.env.user.tz)
        std_tz = tz.gettz('UTC')
        userdatetime = stddatetime.replace(tzinfo=user_tz).astimezone(std_tz).replace(tzinfo=None)
        return userdatetime


class AttendanceCheckout(models.Model):
    _inherit = 'hr.attendance'
    def _process_attendance_checkout(self):
        afternoon_time =''
        formatted_date =''
        create_date = datetime.datetime.now()
        attendance_ids = self.env['hr.attendance'].search([('check_out', '=', False)])
        print(attendance_ids)

        for rec in attendance_ids:
            print(rec,'hhhh')
            if not rec.employee_id.overt_time:
                create_date_utime = rec.employee_id.covert_time_to_user_tz(create_date)
                user_tz = pytz.timezone(self.env.context.get('tz') or rec.employee_id.tz)
                date_today = pytz.utc.localize(create_date).astimezone(user_tz)

                create_weekday = date_today.weekday()
                working_calendar = rec.employee_id.resource_calendar_id
                create_day_schedule = working_calendar.attendance_ids.filtered(
                    lambda d: int(d.dayofweek) == int(create_weekday))
                create_afternoon_time = create_day_schedule.filtered(lambda d: d.day_period == 'afternoon')
                hours = int(create_afternoon_time.hour_to)
                minutes = int((create_afternoon_time.hour_to - hours) * 60)
                afternoon_datetime = datetime.datetime(create_date.year, create_date.month, create_date.day, hours, minutes)
                time = afternoon_datetime.time()
                afternoon_time = time.strftime('%H:%M:%S')


                formatted_date = date_today.strftime('%H:%M:%S')
                if formatted_date == afternoon_time or  formatted_date > afternoon_time:
                    time_difference = datetime.timedelta(hours=5, minutes=30)
                    rec.check_out = afternoon_datetime -time_difference
                    print(rec.check_out,'today')



