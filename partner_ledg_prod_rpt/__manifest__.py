# -*- coding: utf-8 -*-
{
    'name': "Partner Ledger item  Wise Report",
    'summary': """Partner Ledger item  Wise Report""",
    'description': """
        Partner Ledger item  Wise Report
    """,
    'author': "Blueeast",
    'website': "https://blueeast.com/",
    'category': 'Uncategorized',
    'version': '0.1',
    'depends': ['base', 'account', 'contacts'],
    'data': [
        'wizard/wizard.xml',
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'reports/report_template.xml',
        'reports/reports.xml',

    ],
    'demo': [
        'demo/demo.xml',
    ],
}
