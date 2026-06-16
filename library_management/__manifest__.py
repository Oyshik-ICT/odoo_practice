{
    "name": "Library Management",
    "version": "19.0.1",
    "summary": "Library management module for books and members",
    "description": "A odoo module to manage books and members",
    "depends": ["base"],
    "data": [
        "views/library_book_views.xml",
        "views/library_member_views.xml",
        "views/menu.xml",
    ],
    "license": "LGPL-3",
    "sequence": -10,
    "application": True,
}
