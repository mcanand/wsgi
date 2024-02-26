import pytz
from datetime import datetime, timedelta

from odoo import models, fields, api

#
# class Employee(models.Model):
#     _inherit = "hr.employee.public"
#
#     overt_time = fields.Boolean(string="OverTime Permit")
#     exit_progress = fields.Float(string='Exit Progress', default=0.0)
#     entry_progress = fields.Float(string='Entry Progress', default=0.0)
#     maximum_rate = fields.Float(string='Maximum Rate', default=0.0)
#     check_list_enable = fields.Boolean()
#     employee_code = fields.Char()
#     home_country_street = fields.Char()
#     home_country_street2 = fields.Char()
#     home_country_city = fields.Char()
#     home_country_state_id = fields.Many2one('res.country.state', string=" State",
#                                             domain="[('country_id', '=?', home_address_country_id)]")
#     home_country_zip = fields.Char(string="Zip", )
#     home_address_country_id = fields.Many2one('res.country', string="Country")
#     home_country_phone = fields.Char('Contact Number')
#
#     local_street = fields.Char(string="Address")
#     local_street2 = fields.Char(string="Street2")
#     local_city = fields.Char(string="City")
#     local_state_id = fields.Many2one('res.country.state', string=" State",
#                                      domain="[('country_id', '=?', local_country_id)]")
#     local_zip = fields.Char(string="Zip", )
#     local_country_id = fields.Many2one('res.country', string="Country")
#     local_phone = fields.Char('Contact Number')
#     local_email = fields.Char(string="Email")
#     is_manager = fields.Boolean(string="Manager")
#     is_hod = fields.Boolean(string="Department Head")
#     employee_type_id = fields.Many2one('hr.emp.type', string="Employee Type")
#     # emp_education_line_id = fields.One2many('employee.education.line', 'employee_id', string="Education Details")
#     personal_mobile = fields.Char(
#         string='Mobile',
#         store=True,
#         help="Personal mobile number of the employee")
#     joining_date = fields.Date(
#         string='Joining Date',
#         help="Employee joining date computed from the contract start date",
#         )
#     id_expiry_date = fields.Date(
#         string='Expiry Date',
#         help='Expiry date of Identification ID')
#     passport_expiry_date = fields.Date(
#         string='Expiry Date',
#         help='Expiry date of Passport ID')
#     insurance_percentage = fields.Char(string="Company Percentage ", help="Company insurance percentage")
    # id_attachment_id = fields.Many2many(
    #     'ir.attachment', 'id_attachment_rel',
    #     'id_ref', 'attach_ref',
    #     string="Attachment",
    #     help='You can attach the copy of your Id')
    # passport_attachment_id = fields.Many2many(
    #     'ir.attachment',
    #     'passport_attachment_rel',
    #     'passport_ref', 'attach_ref1',
    #     string="Attachment",
    #     help='You can attach the copy of Passport')
    # fam_ids = fields.One2many(
    #     'hr.employee.family', 'employee_id',
    #     string='Family', help='Family Information')


class HrAttendance(models.Model):
    _inherit = 'hr.attendance'
    _description = 'Auto Checkout Cron Job'

    check = fields.Datetime()

    @api.model
    def auto_checkout_employees(self):
        auto_log_off_time = self.env['ir.config_parameter'].sudo().get_param('auto_log_off.auto_log_off_time')

        # Convert auto_log_off_time to a datetime object
        auto_log_off_datetime = datetime.strptime(auto_log_off_time, '%H:%M')
        tz = pytz.timezone('UTC')

        # Get the current date and time
        now = fields.Datetime.now()
        now_utc = pytz.utc.localize(now)

        # Perform auto-checkout for employees who checked in today
        employees_to_checkout = self.env['hr.attendance'].search([
            ('check_in', '>=', now_utc.replace(hour=0, minute=0, second=0)),
            ('check_in', '<', now_utc),('check_out','=',False)
        ])

        for employee in employees_to_checkout:
            tz = pytz.timezone(employee.employee_id.user_id.tz)
            now_tz = now_utc.astimezone(tz)
            checkout_datetime_today = datetime(
                year=now_tz.year,
                month=now_tz.month,
                day=now_tz.day,
                hour=auto_log_off_datetime.hour,
                minute=auto_log_off_datetime.minute,
                second=0,
                microsecond=0,
            )
            if now_tz.replace(tzinfo=None) >= checkout_datetime_today:
                print("datetime", checkout_datetime_today)
                time_difference = timedelta(hours=4, minutes=0)
                employee.write({'check_out': checkout_datetime_today - time_difference})
        return True
