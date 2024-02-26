# -*- coding: utf-8 -*-

{
    'name': 'Open HRMS Employee Insurance',
    'version': '15.0.1.0.0',
    'summary': """Employee Insurance Management for Open HRMS.""",
    'description': """Manages insurance amounts for employees to be deducted from salary""",
    'category': 'Generic Modules/Human Resources',
    'author': 'Dev innovations',
    'website': 'devinnovations.in',
    'depends': [
                'base', 'hr', 'hr_employee_updation'],
    'data': [
        'security/ir.model.access.csv',
        'security/hr_insurance_security.xml',
        'views/employee_insurance_view.xml',
        # 'views/insurance_salary_stucture.xml',
        'views/policy_management.xml',
              ],
    'images': ['static/description/banner.png'],
    'license': 'AGPL-3',
    'installable': True,
    'auto_install': False,
    'application': False,
}
