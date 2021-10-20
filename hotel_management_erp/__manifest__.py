{
    'name': 'HotelErp',
    'version': '1.0.0',
    'sequence': 90,
    'summary': 'Track your Hotel pipeline',
    'description': "",
    'website': 'https://www.odoo.com/page/recruitment',
    'depends': [
        'base','sale'
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/rooms_info.views.xml',
        'views/other_info_views.xml',
        'views/sale_info_views.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
    'license': 'LGPL-3',
}