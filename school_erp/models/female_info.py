from odoo import api, fields, models


class FemaleInfo(models.Model):
    _name = 'female.info'

    # female_ids = fields.One2many(comodel_name='student.info', inverse_name='female_id')
    female_id = fields.Many2one(comodel_name='student.info')