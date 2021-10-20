from odoo import api, fields, models

class Inherit(models.Model):
    _inherit = 'teacher.info'
    teacher_id_no = fields.Integer("Teacher ID No.")