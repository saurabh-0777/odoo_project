from odoo import api, fields, models

class TeacherInfo(models.Model):
    _name = 'teacher.info'

    name = fields.Char('Name',required=True)
    middle_name = fields.Char('Middle Name')
    teacher_age = fields.Integer('Age')
    teacher_std = fields.Selection([('std_1', 'Subject 1'),
                                    ('std_2', 'Subject 2'),
                                    ('std_3', 'Subject 3'),
                                    ('std_4', 'Subject 4'),],
                                      'Subject', required=True)
    city = fields.Char('City', default='Mumbai', readonly =True)
    gender_male = fields.Selection([('male', 'Male'),
                                    ('female', 'Female')],
                                      'Gender', required=True)
    is_pwd = fields.Boolean('Is Phycially Handiacpped?')

