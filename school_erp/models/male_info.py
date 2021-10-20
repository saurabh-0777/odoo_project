from odoo import api, fields, models

class MaleInfo(models.Model):
    _name = 'male.info'

    # male_ids = fields.One2many(comodel_name='student.info', inverse_name='male_id')
    male_id = fields.Many2one(comodel_name='student.info')
    # name = fields.Char(relate = male_id.name)
    # student_age = fields.Integer(relate = male_id.student_age)
    # quota = fields.Integer(relate = male_id.quota)
    # gender_male = fields.Selection(relate = male_id.gender_male)
    # is_pwd = fields.Boolean(relate = male_id.is_pwd)

