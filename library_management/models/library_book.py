from odoo import fields, models


class LibraryBook(models.Model):
    _name = "library.book"

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
