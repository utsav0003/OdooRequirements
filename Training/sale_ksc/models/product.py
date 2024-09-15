from odoo import models, fields

class Product(models.Model):
    _name = 'product.ksc'
    _description = 'Product'

    name = fields.Char(required=True)
    sku = fields.Char(required=True)
    weight = fields.Float(digits=(6, 2))
    length = fields.Float(digits=(6, 2))
    volume = fields.Float(digits=(6, 2))
    width = fields.Float(digits=(6, 2))
    barcode = fields.Char()
    product_type = fields.Selection([('storable', 'Storable'), ('consumable', 'Consumable'), ('service', 'Service')])
    sale_price = fields.Float(digits=(6, 2), default=1.00)
    cost_price = fields.Float(digits=(6, 2), default=1.00)
    product_category_id = fields.Many2one('product.category.ksc', string='Product Category')
    uom_id = fields.Many2one('product.uom.ksc', string='Unit of Measure')
