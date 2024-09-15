from odoo import models, fields

class ProductCategory(models.Model):
    _name = 'product.category.ksc'
    _description = 'Product Category'

    name = fields.Char(required=True)
    parent_id = fields.Many2one('product.category.ksc', string='Parent Category')
    child_ids = fields.One2many('product.category.ksc', 'parent_id', string='Child Categories')
