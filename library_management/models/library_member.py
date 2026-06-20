from odoo import api, fields, models
from odoo.exceptions import ValidationError


class LibraryMember(models.Model):
    _name = "library.member"
    _description = "Members Information"

    name = fields.Char(string="Name", required=True)
    phone = fields.Char(string="Phone Number", required=True)
    email = fields.Char(string="Email")
    join_date = fields.Date(string="Joining Date", default=fields.Date.today)

    @api.constrains("email")
    def _check_email(self):
        for record in self:
            if record.email and "@" not in record.email:
                raise ValidationError("Email is not valid")
