from odoo import fields, models


class SaleOrder(models.Model):
    _inherit = "sale.order"

    delivery_date = fields.Date(string="Delivery Date")
    responsible_person = fields.Many2one(
        "res.users",
        string="Responsible Person",
    )
