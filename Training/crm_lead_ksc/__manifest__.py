{
    'name': 'CRM Lead KSC',
    'version': '1.0',
    'summary': 'Module to manage CRM leads with custom fields and rules',
    'author': 'Your Name',
    'category': 'Sales',
    'depends': [],  # No other dependencies
    'data': [
        # 'security/crm_lead_security.xml',
        'security/ir.model.access.csv',
        'views/crm_lead_ksc_views.xml',
    ],
    'installable': True,
    'application': True,
}
