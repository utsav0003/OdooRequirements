from odoo import models, fields

class SaleOrderLine(models.Model):
    _name = 'sale.order.line.ksc'
    _description = 'Sale Order Line'

    order_id = fields.Many2one('sale.order.ksc', string='Order No')
    product_id = fields.Many2one('product.ksc', string='Product')
    name = fields.Text(string='Description')
    quantity = fields.Float(digits=(6, 2))
    unit_price = fields.Float(digits=(6, 2))
    state = fields.Selection([('draft', 'Draft'), ('confirmed', 'Confirmed'), ('cancelled', 'Cancelled')], default='draft')
    uom_id = fields.Many2one('product.uom.ksc', string='Unit of Measure')
