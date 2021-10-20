from odoo import api, models, fields


class StockPicking(models.Model):
    _inherit = 'stock.picking'

    pro_name = fields.Char('Product Name')