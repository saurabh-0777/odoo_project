import datetime

from dateutil.relativedelta import relativedelta

from odoo import api, fields, models
from odoo.exceptions import ValidationError
from odoo.fields import Datetime



class Rooms(models.Model):
    _name = 'rooms.info'
    _rec_name = 'room_no'
    room_no = fields.Integer("Room No")
    floor_no = fields.Integer("Floor No")

    @api.onchange('room_no')
    def hotel(self):
        if self.room_no > 10:
            raise ValidationError("your hotel has 10 rooms")

    @api.onchange('floor_no')
    def hotel1(self):
        if self.floor_no > 5:
            raise ValidationError("your hotel has 5 floor")


class saleorder(models.Model):
    _inherit = 'res.partner'


    room_info_ids = fields.One2many(comodel_name='hotel.info', inverse_name='room_id')


class hotel(models.Model):
    _name = 'hotel.info'
    product = fields.Many2one(comodel_name='product.product',string='Product')
    quantity = fields.Integer('Quantity')
    price = fields.Float('Price')
    room_id = fields.Many2one(comodel_name='res.partner')
    uom_qty = fields.Many2one(comodel_name='uom.uom')





class process(models.Model):
    _inherit = 'sale.order'

    verification = fields.Boolean('Verification')
    room = fields.Many2one(comodel_name='rooms.info',string='Room No')

    @api.onchange('partner_id')
    def UpdateOrder(self):
        print("update")
        for rec in self:
            lines = [(5, 0, 0)]
            for line in self.partner_id.room_info_ids:
                val = {
                    'product_id': line.product.id,
                    'product_uom_qty': line.quantity,
                    'product_uom': line.uom_qty,
                    'price_unit': line.price,
                }
                lines.append((0, 0, val))
                print(lines)
            rec.order_line = lines
            return 0
    global available
    available = []
    @api.onchange('room')
    def change_room(self):
        for rec in self.room:
            if rec.room_no in available:
                raise ValidationError('select another room')
            else:
                available.append(rec.room_no)

    def action_confirm(self):
        res = super(process, self).action_confirm()
        if self.state == "sale":
            return {
                'name': ("Create Invoices"),
                'view_mode': 'form',
                'view_type': 'form',
                'view_id': False,
                'res_model': 'sale.advance.payment.inv',
                'type': 'ir.actions.act_window',
                'target': 'new'
            }

    # def create_invoices(self):
    #     sale_order = self.env['sale.order'].browse(self._context.get('active_ids', []))






class checkout(models.Model):
    _inherit = 'sale.order.line'

    in_time = fields.Datetime("In Time")
    out_time = fields.Datetime("Out Time")
    waiting = fields.Float("Waiting Time", compute="_duration", store=True)
    no_of_person = fields.Integer('No Of Person')


    @api.depends('in_time', 'out_time')
    def _duration(self):
        if self.in_time and self.out_time:
            start_time = self.in_time
            close_time = self.out_time
            if self.out_time > self.in_time:
                diff = close_time - start_time
                days, seconds = diff.days, diff.seconds
                hours = days * 24 + seconds // 3600
                self.waiting = hours
            else:
                raise ValidationError('Checkout date should be superior than start day')


            if self.waiting > 0 and self.waiting <= 24:
                self.product_uom_qty = 1
            elif self.waiting > 24:
                self.product_uom_qty = diff.days

            # fmt = '%Y-%m-%d %H:%M:%S'
            # d1 = datetime.datetime.strptime(str(start_time), fmt)
            # d2 = datetime.datetime.strptime(str(close_time), fmt)
            #
            # diff = str(d2 - d1)
            # self.waiting = int(diff[:2]) * 24



# sale.advance.payment.inv