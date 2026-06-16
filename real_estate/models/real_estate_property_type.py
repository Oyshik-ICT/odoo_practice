from odoo import fields, models


class PropertyType(models.Model):
    _name = "estate.property.type"
    _description = "Different types of property"

    name = fields.Char(string="Name")
    property_ids = fields.One2many("real.estate", "property_type_id")
