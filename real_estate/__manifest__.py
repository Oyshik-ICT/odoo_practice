{
    "name": "Real Estate",
    "version": "1.0.1",
    "description": "Real Estate to show available properties",
    "depends": ["crm"],
    "category": "Sales",
    "data": [
        "security/res_groups.xml",
        "security/ir.model.access.csv",
        "views/real_estate_menus.xml",
        "views/real_estate_views.xml",
        "views/estate_property_type_view.xml",
        "views/estate_property_type_menu.xml",
    ],
    "demo": [
        "demo/demo.xml",
    ],
    "license": "LGPL-3",
    "sequence": -10,
    "application": True,
}
