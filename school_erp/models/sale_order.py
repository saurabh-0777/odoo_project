from odoo import api, fields, models


class SaleOrderInfo(models.Model):
    _inherit = 'sale.order'

    order_day_info = fields.Char('Order Day')
    Discount_code = fields.Char('Discount Code')
    customer_email = fields.Char(related='partner_id.email', string='Customer Email')

    def copy(self, default={}):
        global lines
        if not default.get('partner_id'):
            default['partner_id'] = 59
            lines = [(5, 0, 0)]
            val = {
                'product_id': 61
            }
            lines.append((0, 0, val))
        self.order_line = lines
        return super(SaleOrderInfo, self).copy(default)


class Saleorderline(models.Model):
    _inherit = 'sale.order.line'

    product_short_code = fields.Char('Product Short Code')
    # product_category = fields.Many2one(comodel_name='product.template', string="Product Category")
    cat = fields.Char(related = 'product_id.product_tmpl_id.categ_id.name')


class AddDetail(models.Model):
    _inherit = 'sale.order'

    def add_detail(self):
        return True

class Tax(models.Model):
    _inherit = 'sale.order'

    tax_discount = fields.Selection([('10%', '10%'),
                                 ('5%', '5%'), ],
                                'Tax Discount',)

    discount = fields.Float('Discount', readonly=True)



    @api.onchange('tax_discount')
    def discount_amount(self):
        if self.tax_discount == '10%':
            self.discount = ((10*self.amount_untaxed)/100)
            self.amount_total = (self.amount_untaxed - self.discount + self.amount_tax)
        elif self.tax_discount == '5%':
            self.discount = ((5*self.amount_untaxed)/100)
            self.amount_total = (self.amount_untaxed - self.discount + self.amount_tax)
        else:
            self.discount == 0
