from odoo import api, fields, models


class StandardInfo(models.Model):
    _name = 'standard.info'
    _rec_name = 'std_name'
    teacher_name = fields.Char("Teacher name")
    std_name = fields.Char('Standard')

    teacher_id = fields.Many2one('teacher.info', 'Teacher')
    division = fields.Selection([('div_a', 'A'),
                                    ('div_b', 'B'),
                                    ('div_c', 'C'),
                                    ('std_d', 'D'),],
                                      'Division', required=True, related= 'teacher_id.division')

    division = fields.Selection([('div_a', 'A'),
                                 ('div_b', 'B'),
                                 ('div_c', 'C'),
                                 ('std_d', 'D'), ],
                                'Division', required=True)

    students_ids = fields.One2many(comodel_name='student.info', inverse_name='student_id', string='Students')
    scholar_ids = fields.Many2many(comodel_name='scholarship.info', relation='standard_info_scholarship_info_rel',column1='stud_id', column2='scholar_id', string='Groups')





