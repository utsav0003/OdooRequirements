{
    'name': 'Partner Demo KSC',
    'version': '1.0',
    'summary': 'Module to manage customer data',
    'category': 'Contacts',
    'author': 'Utsav',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/res_partner_demo_views.xml',
        'data/res_partner_demo_data.xml',
    ],
    'demo': [],
    'installable': True,
    'auto_install': False,
}
