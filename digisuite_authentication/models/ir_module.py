from odoo import api, fields, models, modules, tools, _
from odoo.http import request
from decorator import decorator
from odoo.exceptions import AccessDenied, UserError
import logging
_logger = logging.getLogger(__name__)
from odoo.exceptions import ValidationError

def assert_log_admin_access(method):
    """Decorator checking that the calling user is an administrator, and logging the call.

    Raises an AccessDenied error if the user does not have administrator privileges, according
    to `user._is_admin()`.
    """

    def check_and_log(method, self, *args, **kwargs):
        user = self.env.user
        origin = request.httprequest.remote_addr if request else 'n/a'
        log_data = (method.__name__, self.sudo().mapped('display_name'), user.login, user.id, origin)
        if not self.env.is_admin():
            _logger.warning('DENY access to module.%s on %s to user %s ID #%s via %s', *log_data)
            raise AccessDenied()
        _logger.info('ALLOW access to module.%s on %s to user %s #%s via %s', *log_data)
        return method(self, *args, **kwargs)

    return decorator(check_and_log, method)

class IRModuleModule(models.Model):
    _inherit = "ir.module.module"

    def button_immediate_install(self):
        authe_module = self.env['ir.module.module'].sudo().search([('name', '=', 'digisuite_authentication')])
        if authe_module.state != 'installed':
            raise ValidationError("Please Install %s module first" %authe_module.display_name)
        authentication_form = self.env['authentication.detail'].sudo().search([('is_activated', '=', True)])
        if not authentication_form:
            return {
                'name': _('Activate DigiSuite'),
                'res_model': 'authentication.detail',
                'type': 'ir.actions.act_window',
                'view_mode': 'form',
                'views': [[self.env.ref('digisuite_authentication.authentication_detail_form_view').id, 'form']],
                'target': 'new',
                'context': {},
            }
        else:
            res = super().button_immediate_install()
            return res


    # @assert_log_admin_access
    # @api.model
    # def update_list(self):
    #     print("pppppppppppppppppppppp")
    #     raise AccessDenied("Pleaseeeeeeeeeeeeeeee")
    #     return super(IRModuleModule, self).update_list()