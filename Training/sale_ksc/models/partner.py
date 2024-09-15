from odoo import models, fields

class Partner(models.Model):
    _name = 'res.partner.ksc'
    _description = 'Partner'

    name = fields.Char()
    street1 = fields.Char()
    street2 = fields.Char()
    country_id = fields.Many2one('res.country', string='Country')
    state_id = fields.Many2one('res.state', string='State')
    city_id = fields.Many2one('res.city', string='City')
    zip = fields.Char()
    email = fields.Char()
    mobile = fields.Char()
    phone = fields.Char()
    photo = fields.Image()
    website = fields.Char()
    active = fields.Boolean(default=True)
    parent_id = fields.Many2one('res.partner.ksc', string='Parent Partner')
    child_ids = fields.One2many('res.partner.ksc', 'parent_id', string='Child Partners')
    address_type = fields.Selection([('invoice', 'Invoice'), ('shipping', 'Shipping'), ('contact', 'Contact')])
