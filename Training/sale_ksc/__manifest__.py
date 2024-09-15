{
    'name': 'Sale KSC',
    'version': '1.0',
    'summary': 'Sales Management Module',
    'description': 'Module for managing sales, products, and orders with detailed views and actions.',
    'author': 'Your Name',
    'website': 'https://www.example.com',
    'category': 'Sales',
    'depends': ['base'],
    'data': [
        # Views and Actions
        'views/product_category_views.xml',
        'views/product_views.xml',
        'views/uom_category_views.xml',
        'views/uom_views.xml',
        'views/partner_views.xml',
        'views/sale_order_views.xml',
        'views/sale_order_line_views.xml',

        # Data files
        'data/partner_data.xml',
        'data/product_data.xml',
        'data/uom_data.xml',

        # Security
        'security/ir.model.access.csv',
        'security/sale_ksc_security.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
