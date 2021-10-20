from odoo import api, fields, models
from odoo.exceptions import UserError, ValidationError


class CulturalFest(models.Model):
    _name = 'cultural.fest'
    _rec_name = 'fest_name'

    fest_name = fields.Char('Festival Name')
    standard_id = fields.Many2one('standard.info','Standard Name')
    number_of_participants = fields.Integer('Number of Participants')
    festival_information =fields.Text('Fest Information')
    competition = fields.Char('Competition')
    fees_amount = fields.Integer('Fees')
    name = fields.Many2one(comodel_name='student.info',string='Name')

    sponser_fest_line_ids = fields.One2many(comodel_name='sponser.fest', inverse_name= 'sponser_fest_id', string='Sponser List')
    competition_fees_line_ids = fields.One2many(comodel_name='competition.fees', inverse_name= 'competition_id', string='Competition')


    def default_get(self, fields):
        res = super(CulturalFest, self).default_get(fields)
        res["fest_name"] = "Symposium"
        res["festival_information"] = "IT fest"
        return res

    # def write(self, values):
    #     lines = []
    #     for rec in values.get('competition_fees_line_ids'):
    #         print("Main record: ", rec)
    #         print("student_fees_ids record: ", rec[1])
    #         for record in rec:
    #             if type(rec[1]) is int:
    #                 fest_line_obj = self.env['competition.fees'].browse(rec[1])
    #                 print("fest_line_obj: ", fest_line_obj)
    #                 if not fest_line_obj.fees_calculate:
    #                     if type(record) is dict:
    #                         print("record: ", record)
    #                         if record.get('fees_amount'):
    #                             val = {
    #                                 'fees_calculate': True,
    #                                 'fees_amount': record.get('fees_amount'),
    #                             }
    #                             lines.append((1, rec[1], val))
    #         if lines:
    #             values.update({"competition_fees_line_ids": lines})
    #     print("values: ", values)
    #     return super(CulturalFest, self).write(values)


    # def write(self, vals):
    #     lines = []
    #     if vals:
    #         val={
    #             'competition': vals.get('competition'),
    #             'fees_amount': vals.get('fees_amount'),
    #             'name': vals.get('name'),
    #         }
    #         lines.append((0, 0, val))
    #     vals.update({'competition_fees_line_ids': lines})
    #     return super(CulturalFest, self).write(vals)

    # def write(self, vals):
    #     print("running")
    #     for rec in self.mapped('competition_fees_line_ids'):
    #         value = rec.name.budget + rec.fees_amount
    #         rec.name.budget = value
    #     return super(CulturalFest, self).write(vals)


class sponser(models.Model):
    _name = 'sponser.fest'
    _rec_name = 'sponser_name'

    sponser_name = fields.Char('Sponser Name')
    contribution = fields.Integer('Contribution')

    sponser_fest_id = fields.Many2one(comodel_name='cultural.fest', string='Sponser Fest')

class CompetitionFees(models.Model):
    _name = 'competition.fees'
    _rec_name = 'competition'

    competition = fields.Char('Competition')
    fees_amount = fields.Integer('Fees')
    fees_calculate = fields.Boolean('Fees Calculate')
    name = fields.Many2one(comodel_name='student.info',string='Name')
    competition_id = fields.Many2one(comodel_name='cultural.fest', string='Competition')

    @api.onchange('fees_amount')
    def onchange_fees_id(self):
        print("asdafafg")
        if self.fees_amount:
            self.name.budget = self.name.budget - self.fees_amount
            self.fees_calculate = True


    def unlink(self):
        print("Unlink is running")
        for record in self:
            print(record)
            for rec in record.name:
                print(rec.budget)
                budget_remained = rec.budget + record.fees_amount
                rec.budget = budget_remained
        return super(CompetitionFees, self).unlink()