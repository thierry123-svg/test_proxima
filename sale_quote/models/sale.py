from odoo import api, fields, models, _


class SaleOrderInherit(models.Model):
    _inherit = 'sale.order'
   
    
    is_lead = fields.Boolean(default=True, store=False)

    def action_quotation_send_price(self):
        ''' Opens a wizard to compose an email, with relevant mail template loaded by default '''
        self.ensure_one()
        template_id = self.env.ref('sale_quote.email_template_edi_sale_price').id
        template = self.env['mail.template'].browse(template_id)
        if template:
            ctx = {
                'default_model': 'sale.order',
                'default_use_template': bool(template_id),
                'default_template_id': template_id,
                'default_composition_mode': 'comment',
                'mark_so_as_sent': True,
                'custom_layout': "mail.mail_notification_paynow",
                'proforma': self.env.context.get('proforma', False),
                'force_email': True,
            }
            return {
                'type': 'ir.actions.act_window',
                'view_mode': 'form',
                'res_model': 'mail.compose.message',
                'views': [(False, 'form')],
                'view_id': False,
                'target': 'new',
                'context': ctx,
            }