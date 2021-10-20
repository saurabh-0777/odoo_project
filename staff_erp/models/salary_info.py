from odoo import api, fields, models


class SalaryInfo(models.Model):
    _name = 'salary.info'
    _rec_name = 'salary'

    name = fields.Many2one(comodel_name='staff.info')
    staff_type = fields.Selection([('std_1', 'teaching'),
                                   ('std_2', 'account'),
                                   ('std_3', 'cleaning'),
                                   ('std_4', 'canteen'), ],
                                  'Staff', required=True)
    salary = fields.Integer('salary')

    salary_id = fields.Many2one(comodel_name='staff.info')
