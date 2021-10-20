# -*- encoding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'SchoolERP',
    'version': '1.0',
    'sequence': 90,
    'summary': 'Track your School pipeline',
    'description': "",
    'website': 'https://www.odoo.com/page/recruitment',
    'depends': [
        'base','sale'
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/student_info_views.xml',
        'views/standard_info_views.xml',
        'views/teacher_info_views.xml',
        # 'views/male_info_views.xml',
        # 'views/female_info_views.xml',
        'views/sports_activity_views.xml',
        'views/library_info_views.xml',
        'views/cultural_fest_views.xml',
        'views/scholarship_info_views.xml',
        'views/subject_info_views.xml',
        'wizard/update_order_line_views.xml',
        'views/sale_order_views.xml',
        'views/weather_info_views.xml',
        'views/transfer_inherit_views.xml',
        'report/student_card.xml',
        'report/report.xml',
        'report/sale_report_inherit.xml',

        'wizard/update_age_wizard_views.xml',

    ],
    'installable': True,
    'auto_install': False,
    'application': True,
    'license': 'LGPL-3',
}
