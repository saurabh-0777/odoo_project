from odoo import api, fields, models

class OrderWizard(models.TransientModel):
    _name = "order.wizard"
    _description = "order Wizard"

    expiration = fields.Datetime('expiration')
    product_ids = fields.One2many(comodel_name='sale.wizard', inverse_name='product_id')

    def order_update(self):
        order_id = self.env['sale.order'].search([('id','=', self.env.context.get('active_id'))])
        order_id.validity_date = self.expiration
        # return 1



        for rec in order_id:
            lines = [(5, 0, 0)]
            for line in self.product_ids:
                val = {
                    'product_id': line.product1_id.id,
                    'name': line.description,
                    'product_uom_qty': line.quantity,
                    'price_unit': line.unit_price,
                }
                lines.append((0, 0, val))
            rec.order_line = lines
            return 0

class SaleWizard(models.TransientModel):
    _name = 'sale.wizard'
    _rec_name = 'product1_id'

    product_id = fields.Many2one(comodel_name='order.wizard')
    product1_id = fields.Many2one(comodel_name='product.product', string='Product')
    description = fields.Char('Description')
    quantity = fields.Float('Quantity')
    unit_price = fields.Float('Unit Price')


