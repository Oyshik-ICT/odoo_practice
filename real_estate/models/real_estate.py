from odoo import api, fields, models
from odoo.exceptions import UserError, ValidationError


class RealEState(models.Model):
    _name = "real.estate"
    _description = "Real Estate Property"
    _order = "price asc"

    name = fields.Char(default="House", required=True)
    description = fields.Text(string="Description")
    active = fields.Boolean(default=True)
    state = fields.Selection(
        selection=[
            ("new", "New"),
            ("received", "Offer Received"),
            ("accepted", "Offer Accepted"),
            ("sold", "Sold"),
            ("cancelled", "Cancelled"),
        ],
        required=True,
        copy=False,
        default="new",
    )

    def _default_date(self):
        return fields.Date.today()

    post_code = fields.Char(string="Post Code")
    date_availability = fields.Date(string="Date Availability", default=_default_date)
    price = fields.Float(string="Price")
    selling_price = fields.Float(string="Selling Price", readonly=True)
    bed_rooms = fields.Integer(string="Bed Rooms")
    living_areas = fields.Integer(string="Living Areas")
    garden = fields.Boolean(string="Garden")
    garden_areas = fields.Integer(string="Garden Areas")
    total_areas = fields.Integer(string="Total Areas", compute="_compute_total_areas")
    garage = fields.Boolean(string="Garage")
    garden_orientation = fields.Selection(
        string="Garden Orientation",
        selection=[
            ("north", "North"),
            ("south", "South"),
            ("east", "East"),
            ("west", "West"),
        ],
    )
    property_type_id = fields.Many2one("estate.property.type")
    currency_id = fields.Many2one(
        "res.currency",
        string="Currency",
        default=lambda self: self.env.company.currency_id,
    )

    _sql_constraints = [
        ("check_price", "CHECK(price > 0)", "Price must be greater than 0")
    ]

    def _compute_total_areas(self):
        for rec in self:
            rec.total_areas = rec.living_areas + rec.garden_areas

    @api.onchange("garden")
    def _onchange_garden(self):
        if not self.garden:
            self.garden_areas = 0
        else:
            self.garden_areas = 100

    def sold_button(self):
        if self.state == "cancelled":
            raise UserError("A cancelled property can't be sold")
        self.state = "sold"

    def cancel_button(self):
        if self.state == "sold":
            raise UserError("A sold property can't be cancelled")
        self.state = "cancelled"

    @api.constrains("price")
    def _check_price(self):
        for record in self:
            if record.price <= 0:
                raise ValidationError("Price must be greater than 0.")
