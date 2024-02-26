# -*- coding: utf-8 -*-
from odoo import fields, models, api, _
from getmac import get_mac_address as gma
import socket
import requests
import xml.etree.ElementTree as ET
import xmltodict
from odoo.exceptions import ValidationError, UserError

class AuthenticationForm(models.TransientModel):
    _name = 'authentication.detail'

    def _get_digi_mac_address(self):
        mac_address = gma()
        return mac_address

    def _get_digi_host_name(self):
        host_name = socket.gethostname()
        return host_name

    activation_key = fields.Char(string="Activation Key")
    auth_build_key = fields.Char(sstring="Buildkey")
    auth_full_name = fields.Char(string="Full Name")
    # auth_country_id = fields.Many2one('res.country', string="Country")
    auth_country_id = fields.Char( string="Country")
    auth_mobile = fields.Char(string="Mobile")
    auth_phone = fields.Char(string="Phone")
    auth_email = fields.Char(string="Email")
    auth_mac_address = fields.Char(string="MAC", default=_get_digi_mac_address)
    auth_host_name = fields.Char(string="Host", default=_get_digi_host_name)
    auth_company_name = fields.Char(string="Comapny Name")
    is_activated = fields.Boolean(string="Activatd")

    def activation_api(self, activation_code):
        url = "http://oldactivationapi.digisuiteerp.com/Activate.asmx?op=ActivateDigisuite_Odoo"

        token = 'e2AOaRku6g8wsRHl7EyIaSHft0AssHe63sObrg2KiKLlgoZMzf70lyTAXnyxkkTJag3FDwfXMnstZ6v7jzcb3bQp5cH9YrBELOqDc4ReT7DDCjV2bqWznuePID23xF9ddVLO6P0iRTduWUj7aiNPxZIBKF0nF5Phnm6luz9hsaob7u3VgM9Tih8yW9jFjCd8Gf6W6ldV1ml6pkf6h3BUyqZ9OYV9nU2Ri2ISH2k7xZHLo3Aj9DQXjOPG6HXCSgzj'

        # ActivationKey = activation_code.activation_key
        # BuildKey = activation_code.
        # Host = activation_code.auth_host_name
        # MAC = activation_code.auth_mac_address
        # FullName = activation_code.auth_full_name
        # CompanyName = activation_code.auth_company_name
        # Country = activation_code.auth_country_id
        # Mobile = activation_code.auth_mobile
        # Phone = activation_code.auth_phone
        # Email = activation_code.auth_email

        payload = ("<?xml version=\"1.0\" encoding=\"utf-8\"?>"
                   "<soap:Envelope xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:soap=\"http://schemas.xmlsoap.org/soap/envelope/\">"
                   "<soap:Body>"
                   "<ActivateDigisuite_Odoo xmlns=\"http://oldactivationapi.digisuiteerp.in//\">"
                   "<ActivationKey>{ActivationKey}</ActivationKey>"
                   "<BuildKey>{BuildKey}</BuildKey>"
                   "<Host>{Host}</Host>"
                   "<MAC>{MAC}</MAC>"
                   "<FullName>{FullName}</FullName>"
                   "<CompanyName>{CompanyName}</CompanyName>"
                   "<Country>{Country}</Country>"
                   "<Mobile>{Mobile}</Mobile>"
                   "<Phone>{Phone}</Phone>"
                   "<Email>{Email}</Email>"
                   "</ActivateDigisuite_Odoo>"
                   "</soap:Body>"
                   "</soap:Envelope>")
        payload = payload.format(ActivationKey=activation_code.activation_key, BuildKey=activation_code.auth_build_key,  Host=activation_code.auth_host_name, MAC=activation_code.auth_mac_address, FullName=activation_code.auth_full_name,
                              CompanyName=activation_code.auth_company_name, Country=activation_code.auth_country_id, Mobile=activation_code.auth_mobile, Phone=activation_code.auth_phone, Email=activation_code.auth_email)
        headers = {
            'Content-Type': 'text/xml',
            'Authorization': 'Bearer %s' % token
        }

        # response = requests.request("POST", url, headers=headers, data=payload)
        response = requests.post(url, headers=headers, data=payload)
        print(response.text)
        soap_rsult = xmltodict.parse(response.content)['soap:Envelope']['soap:Body']
        if 'ActivateDigisuite_OdooResponse' in soap_rsult:
            if 'ActivateDigisuite_OdooResult' in soap_rsult['ActivateDigisuite_OdooResponse']:
                stack_d = soap_rsult['ActivateDigisuite_OdooResponse']['ActivateDigisuite_OdooResult']['string']
                if stack_d[0] == 'True':
                    activation_code.is_activated = True
                if stack_d[0] == 'False':
                    raise UserError(_("Activation Failed"))

    def digi_authen_activation_api(self):
        for rec in self:
            activation_code = self.env['authentication.detail'].sudo().search([('activation_key', '=', rec.activation_key), ('is_activated', '=', False)], limit=1)
            if activation_code:
                rec.activation_api(activation_code)

    @api.model
    def create(self, vals):
        auth = self.env['authentication.detail'].sudo().search([('activation_key', '=', vals['activation_key'])])
        if auth:
            raise ValidationError("Authentication Key Unique")
        return super(AuthenticationForm, self).create(vals)


    # def get_digi_mac_address(self):
    #     for rec in self:
    #         mac_address = gma()
    #         rec.auth_mac_address = mac_address