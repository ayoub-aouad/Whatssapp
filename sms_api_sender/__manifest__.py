# -*- coding: utf-8 -*-
{
    'name': "SMS Sender",
    'summary': """
        This Model allows us to send sms using bulksms apim""",

    'description': """
        This Model allows us to send sms using bulksms api
    """,
    'author': "Osisoftware",
    'website': "https://www.osisoftware.ma",
    'category': 'Contact',
    'version': '0.1',
    'depends': ['base','contacts'],
    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'wizard/sms_sender.xml',
    ],
}
