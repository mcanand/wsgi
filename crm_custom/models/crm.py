import json

from lxml import etree

from odoo import api, models, fields


class UtmSource(models.Model):
    _inherit = 'utm.source'

    is_needed = fields.Boolean()


class UtmMixin(models.AbstractModel):
    _inherit = 'crm.lead'

    source_id = fields.Many2one('utm.source', 'Source',
                                help="This is the source of the link, e.g. Search Engine, another domain, or name of email list",
                                domain=[('is_needed', '=', True)])

    brn_no = fields.Char("Brn No")
    rm_name = fields.Many2one('res.users', 'Rm Name')
    lead_generator = fields.Many2one('res.users', 'Lead Generator', related='create_uid')
    approved_amount = fields.Monetary('Approved Amount',currency_field='company_currency')

