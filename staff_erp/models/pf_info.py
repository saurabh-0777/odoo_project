from odoo import api, fields, models


class PFInfo(models.Model):
    _name = 'pf.info'
    _rec_name = 'name'

    name = fields.Many2one(comodel_name='staff.info')
    joining_date = fields.Date('Joining Date')
    retire_date = fields.Date('Retire Date')
    provident_fund = fields.Integer('Provident Fund')