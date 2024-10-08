{
    'name': 'Employee Management KSC',
    'version': '1.0',
    'summary': 'Employee Management with Departments, Shifts, and Leaves',
    'description': 'Manage employees, departments, shifts, and leaves.',
    'category': 'Human Resources',
    'author': 'Your Name',
    'depends': ['base'],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/menus.xml',
        'views/employee_department_views.xml',
        'views/employee_shift_views.xml',
        'views/employee_views.xml',
        'views/employee_leave_views.xml',
    ],
    'installable': True,
    'application': True,
}
