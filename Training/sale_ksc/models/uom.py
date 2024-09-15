from odoo import models, fields

class UomCategory(models.Model):
    _name = 'product.uom.category.ksc'
    _description = 'UOM Category'

    name = fields.Char()
    uom_ids = fields.One2many('product.uom.ksc', 'uom_category_id', string='Units of Measure')

class Uom(models.Model):
    _name = 'product.uom.ksc'
    _description = 'Unit of Measure'

    name = fields.Char()
    uom_category_id = fields.Many2one('product.uom.category.ksc', string='UOM Category')
