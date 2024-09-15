from odoo import models, fields, api

class CrmLeadKSC(models.Model):
    _name = 'crm.lead.ksc'
    _description = 'CRM Lead KSC'

    customer_name = fields.Char(string='Customer Name', required=True)
    customer_email = fields.Char(string='Customer Email', required=True)
    customer_phone = fields.Char(string='Customer Phone', required=True)
    expected_revenue = fields.Float(string='Expected Revenue', digits=(10, 3))
    salesperson = fields.Char(string='Salesperson', required=True)
    sales_team = fields.Char(string='Sales Team')
    campaign = fields.Char(string='Campaign')
    channel = fields.Selection([
        ('facebook', 'Facebook'),
        ('whatsapp', 'WhatsApp'),
        ('email', 'Email'),
        ('newspaper', 'Newspaper'),
        ('television', 'Television'),
        ('phone_call', 'Phone Call'),
        ('sms', 'SMS'),
        ('google_ads', 'Google Ads')
    ], string='Channel', required=True)
    state = fields.Selection([
        ('new', 'New'),
        ('qualified', 'Qualified'),
        ('proposition', 'Proposition'),
        ('won', 'Won'),
        ('lost', 'Lost')
    ], string='State', default='new', required=True)
    next_follow_up_date = fields.Date(string='Next Follow Up Date', required=True)
    won_date = fields.Date(string='Won Date')
    lost_reason = fields.Text(string='Lost Reason')

    @api.onchange('state')
    def _onchange_state(self):
        if self.state == 'won':
            self.won_date = fields.Date.today()
        else:
            self.won_date = False

    @api.depends('state')
    def _compute_visibility_fields(self):
        for record in self:
            record.show_won_date = record.state == 'won'
            record.show_lost_reason = record.state == 'lost'

    show_won_date = fields.Boolean(compute='_compute_visibility_fields', store=True)
    show_lost_reason = fields.Boolean(compute='_compute_visibility_fields', store=True)
