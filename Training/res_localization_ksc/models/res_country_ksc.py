from odoo import models, fields

class ResCountryKsc(models.Model):
    _name = 'res.country.ksc'
    _description = 'Country'

    name = fields.Char(string='Country Name', required=True)
    short_code = fields.Char(string='Country Code', required=True)
    state_ids = fields.One2many('res.state.ksc', 'country_id', string='States')
