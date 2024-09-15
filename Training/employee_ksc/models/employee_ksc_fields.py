from odoo import models, fields

class EmployeeKSC(models.Model):
    _name = 'employee.ksc'
    _description = 'Employee KSC'

    name = fields.Char(string='Employee Name', required=True)
    department_name = fields.Char(string='Department Name')
    job_position = fields.Char(string='Job Position')
    salary = fields.Float(string='Salary')
    hire_date = fields.Date(string='Hire Date')
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('transgender', 'Transgender')
    ], string='Gender', required=True)
    job_type = fields.Selection([
        ('permanent', 'Permanent'),
        ('adhoc', 'Ad Hoc')
    ], string='Job Type', required=True)
