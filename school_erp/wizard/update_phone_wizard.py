from odoo import api, fields, models

class PhoneWizard(models.TransientModel):
    _name = "phone.wizard"
    _description = "Phone Wizard"


    update_phone = fields.Integer('Update Phone')

    def phone_update(self):
        active_id = self.env.context.get('active_id')
        res_partner_rec = self.env['res.partner']
        res_partner_id = res_partner_rec.search([('id','=', active_id)])
        res_partner_id.phone = self.update_phone
        return 1