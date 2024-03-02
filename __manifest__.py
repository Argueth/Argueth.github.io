# -*- coding: utf-8 -*-
{
    'name': "Gestión de eventos",

    'summary': """
        Un módulo para modularlos a todos.""",

    'description': """
        Módulo para gestionar eventos de tipo audiovisual. Permite crear eventos, editarlos, añadir personal
        y material al evento, añadir notas y temporalización orientativa.
    """,

    'author': "Pablo Giner Barrios",
    'website': "https://github.com/Argueth/gestion_eventos",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','hr'],

    'application':True,
    # always loaded
    'data': [
        #security
        'security/groups.xml',
        'security/ir.model.access.csv',
        #views
        'views/views.xml',
        'views/templates.xml',
        #data
        'data/materials.xml',
        'data/budget_templates.xml',
        'data/lines.xml',
        'data/types.xml',
        #reports
        'reports/materials_report.xml',
        'reports/events_report.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
