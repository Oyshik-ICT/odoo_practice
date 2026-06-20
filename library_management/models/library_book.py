from odoo import api, fields, models
from odoo.exceptions import ValidationError


class LibraryBook(models.Model):
    _name = "library.book"
    _description = "Books Information"

    name = fields.Char(string="Name", required=True)
    author = fields.Char(string="Author", required=True)
    isbn = fields.Char(string="ISBN", required=True)
    total_copies = fields.Integer(string="Total Copies", required=True)
    available_copies = fields.Integer(string="Available Copies", required=True)
    state = fields.Selection(
        selection=[
            ("available", "Available"),
            ("unavailable", "Unavailable"),
        ],
        required=True,
        default="available",
    )

    _sql_constraints = [
        ("unique_isbn", "UNIQUE(isbn)", "ISBN must be unique"),
    ]

    @api.constrains("total_copies", "available_copies")
    def _check_copies(self):
        for record in self:
            if record.total_copies < 0 or record.available_copies < 0:
                raise ValidationError("Copies can't be negative")
            if record.available_copies > record.total_copies:
                raise ValidationError(
                    "Available copies must be less than or equal to total copies"
                )

    def make_unavailable(self):
        for record in self:
            if record.state == "available":
                record.state = "unavailable"
                record.available_copies = 0

    def make_available(self):
        for record in self:
            if record.state == "unavailable":
                record.state = "available"
                record.available_copies = record.total_copies
