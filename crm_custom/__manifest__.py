# -*- coding: utf-8 -*-
{
    'name': 'CRM Custom',
    'summary': 'CRM Custom',
    'version': '15.0.1.0.0',
    'description': """CRM Custom""",
    'author': 'Vrindha Vinoj',
    'installable': True,
    'depends': ['mail', 'base', 'crm', 'crm_iap_mine','utm'],
    'demo': [
    ],
    'data': [
        'views/pipeline_tree.xml'
    ],
    'assets': {
        'web.assets_qweb': [
            'crm_custom/static/src/xml/**/*',
        ],
    },
    'installable': True,
    'application': True,
}
