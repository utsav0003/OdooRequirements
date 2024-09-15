from odoo import models, fields

class EmployeeLeaveKsc(models.Model):
    _name = 'employee.leave.ksc'
    _description = 'Employee Leave'

    employee_id = fields.Many2one('employee.ksc', string='Employee', required=True)
    department_id = fields.Many2one('employee.department.ksc', string='Department')
    start_date = fields.Date(string='Start Date', required=True)
    end_date = fields.Date(string='End Date', required=True)
    status = fields.Selection([
        ('draft', 'Draft'),
        ('approved', 'Approved'),
        ('refused', 'Refused'),
        ('cancelled', 'Cancelled')
    ], string='Status', default='draft')
    leave_description = fields.Char(string='Leave Description', required=True)
