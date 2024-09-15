from odoo import models, fields

class EmployeeDepartmentKsc(models.Model):
    _name = 'employee.department.ksc'
    _description = 'Employee Department'

    name = fields.Char(string='Department Name', required=True)
    employee_ids = fields.One2many('employee.ksc', 'department_id', string='Employees')
    department_manager_id = fields.Many2one('res.users', string='Department Manager')
