from odoo import api, fields, models

class LibraryInfo(models.Model):
    _name = 'library.info'
    _rec_name = "book_name"

    book_name = fields.Char('book_name')
    book_author = fields.Char('book_author')
    book_issue_date = fields.Datetime('book_issue_date')
    book_return_date = fields.Datetime('book_return_date')

    library_ids = fields.One2many(comodel_name='student.info', inverse_name='student1_id', string='Students')


    @api.model
    def create(self, vals):
        print('CREATE CALL', vals)
        print('Create working')
        vals['book_author'] = 'Mystery'
        return super(LibraryInfo, self).create(vals)

    def write(self, vals):
        print('Vals', vals)
        if vals:
            vals.update({'book_author': 'JASSICA'})
        return super(LibraryInfo, self).write(vals)
