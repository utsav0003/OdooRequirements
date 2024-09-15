{
    'name': 'Localization Module KSC',
    'version': '1.0',
    'summary': 'Country, State, and City Management',
    'description': 'Module to manage countries, states, and cities localization.',
    'category': 'Localization',
    'author': 'Your Name',
    'depends': ['base'],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/menus.xml',
        'views/res_country_views.xml',
        'views/res_state_views.xml',
        'views/res_city_views.xml',
    ],
    'installable': True,
    'application': True,
}
