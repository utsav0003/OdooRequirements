from odoo import models, fields

class SaleOrder(models.Model):
    _name = 'sale.order.ksc'
    _description = 'Sale Order'

    name = fields.Char(required=True, string='Order No')
    customer_id = fields.Many2one('res.partner.ksc', string='Customer', domain="[('address_type', '=', 'contact')]")
    invoice_customer_id = fields.Many2one('res.partner.ksc', string='Invoice Customer', domain="[('address_type', '=', 'invoice')]", required=True)
    shipping_customer_id = fields.Many2one('res.partner.ksc', string='Shipping Customer', domain="[('address_type', '=', 'shipping')]", required=True)
    sale_order_date = fields.Date(string='Sale Order Date')
    order_line_ids = fields.One2many('sale.order.line.ksc', 'order_id', string='Order Lines')
    salesperson_id = fields.Many2one('res.users', string='Salesperson')
    state = fields.Selection([('draft', 'Draft'), ('confirmed', 'Confirmed'), ('done', 'Done'), ('cancelled', 'Cancelled')], default='draft')
