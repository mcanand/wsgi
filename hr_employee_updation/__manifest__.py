# -*- coding: utf-8 -*-
{
    'name': 'Open HRMS Employee Info',
    'version': '15.0.1.1.0',
    'summary': """Adding Advanced Fields In Employee Master""",
    'description': 'This module helps you to add more information in employee records.',
    'category': 'Generic Modules/Human Resources',
    'author': "Dev innovations",
    'website': "devinnovations.in",
    'depends': ['base', 'hr', 'mail', 'hr_gamification', 'hr_contract', 'hr_employee_custom'],
    'data': [
        'data/data.xml',
        'security/ir.model.access.csv',
        'data/hr_notification.xml',
        'views/contract_days_view.xml',
        'views/updation_config.xml',
        'views/hr_employee_view.xml',
    ],
    'images': ['static/description/banner.png'],
    'license': 'AGPL-3',
    'installable': True,
    'auto_install': False,
    'application': False,
}
