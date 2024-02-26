from odoo import models, fields

class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    auto_checkout_all_employees = fields.Boolean(
        string='Auto Checkout All Employees',
        config_parameter='auto_log_off.auto_checkout_all_employees',
    )

    auto_log_off_time = fields.Selection([
        ('00:00', '00:00'), ('01:00', '01:00'), ('02:00', '02:00'), ('03:00', '03:00'),
        ('04:00', '04:00'), ('05:00', '05:00'), ('06:00', '06:00'), ('07:00', '07:00'),
        ('08:00', '08:00'), ('09:00', '09:00'), ('10:00', '10:00'), ('11:00', '11:00'),
        ('12:00', '12:00'), ('13:00', '13:00'), ('14:00', '14:00'), ('15:00', '15:00'),
        ('16:00', '16:00'), ('17:00', '17:00'), ('18:00', '18:00'), ('19:00', '19:00'),
        ('20:00', '20:00'), ('21:00', '21:00'), ('22:00', '22:00'), ('23:00', '23:00'),
    ], string='Auto Check Out Time', config_parameter='auto_log_off.auto_log_off_time',
       help="Select the time for auto-checkout in 24-hour format.")
