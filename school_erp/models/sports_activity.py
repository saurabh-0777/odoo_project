from odoo import api, fields, models

class SportsActivity(models.Model):
    _name = 'sports.activity'

    name = fields.Char('Game')
    sports_type = fields.Selection([('outdoor', 'Outdoor'),
                                    ('indoor', 'Indoor'),],
                                      'Sports Type',)

