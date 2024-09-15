from odoo import models, fields

class ResStateKsc(models.Model):
    _name = 'res.state.ksc'
    _description = 'State'

    name = fields.Char(string='State Name', required=True)
    short_code = fields.Char(string='State Code', required=True)
    country_id = fields.Many2one('res.country.ksc', string='Country', required=True)
    city_ids = fields.One2many('res.city.ksc', 'state_id', string='Cities')
