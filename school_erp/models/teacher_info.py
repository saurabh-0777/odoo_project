from odoo import api, fields, models


class TeacherInfo(models.Model):
    _name = 'teacher.info'
    _rec_name = 'teacher_name'
    teacher_name = fields.Char('teacher_Name')
    Surname = fields.Char('Surname')
    teachers_age = fields.Integer('Age')
    standard_id = fields.Selection([('std_1', 'Standard 1'),
                                    ('std_2', 'Standard 2'),
                                    ('std_3', 'Standard 3'),
                                    ('std_4', 'Standard 4'),],
                                       'Standard',)
    city = fields.Char('City', default ='Mumbai', readonly =True)
    gender = fields.Selection([('male', 'Male'),
                                    ('female', 'Female')],
                                      'Gender', )
    is_pwd = fields.Boolean('is available fulltime ')

    division = fields.Selection([('div_a', 'A'),
                                    ('div_b', 'B'),
                                    ('div_c', 'C'),
                                    ('std_d', 'D'),],
                                      'Division', )

    subject = fields.Many2one(comodel_name='subject.info')
    teacher_id = fields.Many2one('teacher.info', 'Teacher')

class SubjectInfo(models.Model):
    _name = 'subject.info'
    _rec_name = 'subject_name'

    subject_name = fields.Char("Subject Name")

