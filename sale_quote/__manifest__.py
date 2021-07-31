# -*- coding: utf-8 -*-
{
    'name': "sale_quote",

    'summary': """
       Module pour envoyer les devis sans prix aux clients!!""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Thierry Zock",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'sale'],

    # always loaded
    'data': [ 
        'views/sale_views.xml',
        'report/report.xml',
        'report/sale_view_template.xml',
        'data/mail_data.xml',
        # 'security/ir.model.access.csv',
        # 'views/views.xml',
        # 'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}