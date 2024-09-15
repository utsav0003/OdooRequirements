from odoo import models, fields, api

class ResPartnerDemo(models.Model):
    _name = 'res.partner.demo1'
    _description = 'Partner Demo'

    name = fields.Char(string='Name', required=True)
    email = fields.Char(string='Email')
    street1 = fields.Char(string='Street 1')
    street2 = fields.Char(string='Street 2')
    city = fields.Char(string='City')
    state = fields.Char(string='State')
    zip_code = fields.Char(string='Zip Code')
    country = fields.Char(string='Country')
    birthdate = fields.Date(string='Birthdate')
    age = fields.Integer(string='Age')
    weight = fields.Float(string='Weight')
    description = fields.Text(string='Description')
    gender = fields.Selection(
        [('male', 'Male'), ('female', 'Female'), ('transgender', 'Transgender')],
        string='Gender'
    )
    details = fields.Html(string='Details')
    is_spectacles = fields.Boolean(string='Has Spectacles')
    photo = fields.Image(string='Photo')
