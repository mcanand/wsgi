# -*- coding: utf-8 -*-
{
    'name': 'Auto Log Off',
    'summary': 'CRM Custom',
    'version': '15.0.1.0.0',
    'description': """""",
    'author': 'Code 98 Solutions',
    'installable': True,
    'depends': ['base', 'hr_attendance'],
    'demo': [
    ],
    'data': [
        'data/cron.xml',
        'views/res_config.xml'
    ],
    'license': 'AGPL-3',
    'installable': True,
    'auto_install': False,
    'application': True,
}
