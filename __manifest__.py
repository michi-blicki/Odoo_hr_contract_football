# -*- coding: utf-8 -*-
{
    'name': "HR Contract Football",

    'summary': "Add football specific contract values and legal notes to hr.contract",

    'description': """
This module adds football specific contract values and legal notes to hr.contract. 
It also adds a new payroll structure type for football trainers and players.
Football icon of Odoo HR Contract Football module by https://www.flaticon.com/de/kostenloses-icon/fussball_2817805.
    """,

    'author': "Odoo Community Association (OCA), Michael Blickenstorfer",
    'website': "https://github.com/OCA/hr",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Human Resources',
    'version': '18.0.1.0.0',
    'license': "AGPL-3",
    'application': False,
    'auto_install': False,
    'installable': True,

    # any module necessary for this one to work correctly
    'depends': ['hr_contract', 'payroll', 'mail'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'data/ressource_calendar.xml',
        'data/hr_payroll_structure_type.xml',
        'views/view_hr_contract_football_condition.xml',
        'views/view_hr_contract_form_football.xml',
    ],

    #
    # Hooks
    #'pre_init_hook': 'pre_init_hook',
    #'post_init_hook': 'post_init_hook',
    #'uninstall_hook': 'uninstall_hook',
}

