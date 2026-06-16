from odoo import fields, models


class LibraryMember(models.Model):
    _name = "library.member"

    name = fields.Char(string="Name", required=True)
    phone = fields.Char(string="Phone Number", required=True)
    email = fields.Char(string="Email")
    join_date = fields.Date(string="Joining Date", default=fields.Date.today)
