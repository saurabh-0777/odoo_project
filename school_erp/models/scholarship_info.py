from odoo import api, fields, models

class Scholarship_info(models.Model):
    _name = 'scholarship.info'
    _rec_name = "scholarship_name"

    scholarship_name = fields.Char('Scholarship_name')
    student_name = fields.Char('Student_name')
    # standard_id = fields.Many2one('standard.info','Standard')
    # division1 = fields.Selection([('div_a', 'A'),
    #                              ('div_b', 'B'),
    #                              ('div_c', 'C'),
    #                              ('std_d', 'D'), ],
    #                             'Division', )


