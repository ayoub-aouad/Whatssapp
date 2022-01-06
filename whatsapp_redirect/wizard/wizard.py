# -*- coding: utf-8 -*-

from odoo import models, api, fields
from wati_api import client


class WhatsappSendMessage(models.TransientModel):

    _name = 'whatsapp.message.wizard'
    _description = "Whatsapp Wizard"

    mobile = fields.Char(string='Mobile', required=True)
    message = fields.Text(string="message", required=True)
    token  = fields.Char(string='Token', required=True, )
    
    def send_whatssapp_message(self):
        endpoint = 'https://app-server.wati.io'
        wa_client = client.Client(endpoint,self.token)
        return wa_client.send_session_message(whatsapp_number=self.mobile, message_text=self.message)
  

