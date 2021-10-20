from odoo import api, fields, models
from odoo.exceptions import AccessError, UserError, RedirectWarning, ValidationError, Warning



class StudentInfo(models.Model):
    _name = 'student.info'

    name = fields.Char('Name' , required=True)
    middle_name = fields.Char('Middle Name')
    full_name = fields.Char('Full Name', compute='_compute_full_name', store=True)
    student_age = fields.Integer('Age')
    quota = fields.Selection([('twenty_five' , '25%'),
                              ('ten', '10%')],
                             'Quota')


    city = fields.Char('City', default ='Mumbai', readonly =True)
    gender_male = fields.Selection([('male', 'Male'),
                                    ('female', 'Female')],
                                      'Gender')
    is_pwd = fields.Boolean('Is Phycially Handiacpped?')

    standard_id = fields.Many2one('standard.info', 'Standard')
    division = fields.Selection([('div_a', 'A'),
                                    ('div_b', 'B'),
                                    ('div_c', 'C'),
                                    ('std_d', 'D'),],
                                      'Division', required=True, related='standard_id.division')
    budget = fields.Integer('Budget', readonly=0, store=True)
    teacher_name = fields.Char(related='standard_id.teacher_name')
    student_id = fields.Many2one(comodel_name='standard.info')
    sports_id = fields.Many2one(comodel_name='sports.activity', string='Game', )
    student1_id = fields.Many2one(comodel_name='library.info')


    book_author = fields.Char('book_author')
    book_issue_date = fields.Datetime('book_issue_date')
    book_return_date = fields.Datetime('book_return_date')

    fest_ids = fields.Many2many(comodel_name='cultural.fest', relation= 'student_info_cultural_fest_rel', column1= 'stud_id', column2='fest_id', string='Groups')
    scholarship_ids = fields.Many2many(comodel_name='scholarship.info', relation= 'student_info_scholarship_info_rel', column1='stud_id', column2='scholarship_id', string='scholarship')

    teacher_ids = fields.One2many(comodel_name='teachers.subjects.line', inverse_name='teacher1_id')
    fees_ids = fields.One2many(comodel_name='competition.fees', inverse_name='name')




    chemistry = fields.Integer('Chemistry')
    physics = fields.Integer('Physics')
    math = fields.Integer('Math')
    english = fields.Integer('English')
    hsc = fields.Integer('HSc Total', readonly= True)
    hsc_percent = fields.Float('HSc Percent', readonly=True)
    status = fields.Char('Status', readonly=True)
    documents = fields.Binary('Documents')
    timetable = fields.Html('Time Table')

    @api.onchange('chemistry', 'physics', 'math', 'english')
    def total(self):
        print('compute')
        if self.chemistry and self.physics and self.math and self.english:
            self.hsc = self.chemistry + self.physics + self.math + self.english

    @api.onchange('hsc')
    def percent(self):
        self.hsc_percent = (self.hsc / 400) * 100

        if self.hsc_percent > 40:
            self.status = 'Pass'
        elif self.hsc_percent < 40:
            self.status = 'Fail'


    @api.depends('name', 'middle_name')
    def _compute_full_name(self):
        print('in compute')
        if self.name and self.middle_name:
            self.full_name = self.name + " " + self.middle_name

    # @api.depends('fees_ids')
    # def _compute_inherited_class(self):
    #     for rec in self.mapped('fees_ids'):
    #         if rec.fees_calculate == False:
    #             rem = self.budget - rec.fees_amount
    #             self.budget = rem
    #             rec.fees_calculate = True

    # def write(self, vals):
    #     print("sffswv")
    #     for rec in self.mapped('fees_ids'):
    #         if rec.fees_calculate == False:
    #             rem = self.budget - rec.fees_amount
    #             self.budget = rem
    #             rec.fees_calculate = True
    #         return super(StudentInfo, self).write(vals)


    # @api.onchange('fees_id')
    # def amount(self):
    #     print('running')
    #     for record in self.fees_id:
    #         if self.budget >= record.fees_amount:
    #             x = self.budget - record.fees_amount
    #             self.budget = x
    #         else:
    #             raise UserError('Your Budget is too low')
    #

    def change_age(self):
        self.student_age = 25
        return 1

    @api.onchange('is_pwd')
    def onchange_quota(self):
        if self.is_pwd == True:
            self.quota = 'twenty_five'
        else:
            self.quota = 'ten'

    # male_id = fields.Many2one(comodel_name='male.info')
    # female_id = fields.Many2one(comodel_name='female.info')


class TeachersSubjects(models.Model):
    _name = 'teachers.subjects.line'

    teacher1_id = fields.Many2one(comodel_name='student.info')

    subject_id = fields.Many2one(comodel_name='subject.info', string="Subjects")

    teacher_name_id = fields.Many2one(comodel_name='teacher.info')

