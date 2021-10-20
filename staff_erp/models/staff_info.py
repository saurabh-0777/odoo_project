from odoo import api, fields, models


class StaffInfo(models.Model):
    _name = 'staff.info'

    name = fields.Char('Name',required=True)
    middle_name = fields.Char('Middle Name')
    staff_age = fields.Integer('Age')
    staff_type = fields.Selection([('std_1', 'teaching'),
                                    ('std_2', 'account'),
                                    ('std_3', 'cleaning'),
                                    ('std_4', 'canteen'),],
                                      'Staff', required=True)
    city = fields.Char('City', default='Mumbai', readonly =True)
    gender_male = fields.Selection([('male', 'Male'),
                                    ('female', 'Female')],
                                      'Gender', required=True)
    is_pwd = fields.Boolean('Is Phycially Handiacpped?')

    salary_ids = fields.One2many(comodel_name='salary.info', inverse_name='name', string='Salary')

    pf_ids = fields.Many2many(comodel_name='pf.info', relation='staff_info_pf_info_rel',
                                       column1='pf_id', column2='amount', string='Provident Fund')
