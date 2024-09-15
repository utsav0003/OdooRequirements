from odoo import models, fields

class EmployeeKsc(models.Model):
    _name = 'employee.ksc'
    _description = 'Employee'

    name = fields.Char(string='Name of the Employee', required=True)
    department_id = fields.Many2one('employee.department.ksc', string='Department', required=True)
    shift_id = fields.Many2one('employee.department.shift.ksc', string='Shift', required=True)
    job_position = fields.Char(string='Job Position')
    salary = fields.Float(string='Salary', digits=(6, 2))
    hire_date = fields.Date(string='Hire Date')
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('transgender', 'Transgender')
    ], string='Gender')
    job_type = fields.Selection([
        ('permanent', 'Permanent'),
        ('ad_hoc', 'Ad Hoc')
    ], string='Job Type')
    is_manager = fields.Boolean(string='Is Manager')
    manager_id = fields.Many2one('employee.ksc', string='Manager', domain="[('is_manager', '=', True)]", readonly=True)
    related_user_id = fields.Many2one('res.users', string='Related User')
    employee_ids = fields.One2many('employee.ksc', 'manager_id', string='Employees under Manager', readonly=True)
    increment_percentage = fields.Float(string='Increment Percentage', digits=(6, 2), groups='employee_mgmt_ksc.group_employee_manager')
