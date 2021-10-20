from odoo import api, fields, models

class StudentWizard(models.TransientModel):
    _name = "student.wizard"
    _description = "Student Wizard"


    update_age = fields.Integer('Update Age')

    def age_update(self):
        active_id = self.env.context.get('active_id')
        student_info_rec = self.env['student.info']
        student_changee_id = student_info_rec.search([('id','=', active_id)])
        student_changee_id.student_age = self.update_age
        return 1
