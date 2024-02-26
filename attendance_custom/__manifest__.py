# -*- coding: utf-8 -*-

{
    'name': 'Custom Attendance',
    'version': '15.0.1.0.0',
    'summary': """Attendance Over Time Permission""",
    'description': 'Attendance Over Time Permission',
    'category': 'Generic Modules/Human Resources',
    'author': 'Dev Innovations',
    'company': 'Dev Innovations',
    'website': "www.devinnovations.in",
    'depends': ['base_setup', 'hr_holidays','hr_attendance'],
    'data': [
        'views/attendance.xml',
        'data/crone_data.xml'
    ],
    'images': ['static/description/bannerr.png'],
    'license': "AGPL-3",
    'installable': True,
    'auto_install': False,
    'application': False,
}
