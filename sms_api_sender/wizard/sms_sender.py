from odoo import models, fields,_
import requests


class SmsGatewaySender(models.TransientModel):
    _name = "sms.gateway.api"

    tel  = fields.Char(string='Tel',default='0661415410',readonly=True)
    token  = fields.Char(string='Token',default='9agBmGbLKM77t7NnPGPQJwipi',readonly=True)
    message  = fields.Text(string='Massage')

    def notification(self,title,message,type_):
        notification = {
            'type': 'ir.actions.client',
            'tag': 'display_notification',
            'params': {
                'title': (title),
                'message': message ,
                'type':type_,
                'sticky': True, 
            },}
        return notification

    def send_sms(self):
            url = 'https://bulksms.ma/developer/sms/send'+'?token='+self.token+'&message='+self.message+'&tel='+self.tel
            r = requests.get(url)
            if r.status_code == 200:
                return self.notification('SMS SENDER','Your SMS has been sent Successfully','success')
            else:
                return self.notification('SMS SENDER','Something Wrong','warning')

   
