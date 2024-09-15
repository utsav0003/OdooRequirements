from odoo import models, fields

class ProductKSC(models.Model):
    _name = 'product.ksc'
    _description = 'Product KSC'

    name = fields.Char(string='Product Name', required=True)
    sku = fields.Char(string='SKU')
    barcode = fields.Char(string='Barcode')
    can_be_sold = fields.Boolean(string='Can be Sold')
    product_type = fields.Selection([
        ('storable', 'Storable'),
        ('consumable', 'Consumable'),
        ('service', 'Service')
    ], string='Product Type', required=True)
    sale_price = fields.Float(string='Sale Price')
    cost_price = fields.Float(string='Cost Price')
    active = fields.Boolean(string='Active', default=True)
    warehouse = fields.Char(string='Warehouse')
    product_image = fields.Image(string='Product Image')
    website_description = fields.Html(string='Website Description')
    internal_note = fields.Text(string='Internal Note')
