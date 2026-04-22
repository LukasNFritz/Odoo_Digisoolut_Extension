# -*- coding: utf-8 -*-
# Part of Softhealer Technologies.
{
    "name": "All In One Merge PDF Attachment | Invoice Merge PDF Attachment",
    "author": "Softhealer Technologies",
    "website": "https://www.softhealer.com",
    "support": "support@softhealer.com",
    "category": "Extra Tools",
    "version": "17.0.2.0",
    "summary": "Merge PDF Attachment, Merge Attachments In Report,Account Merge PDF Attachment",
    "description": """This module allows to merge PDF attachments with the invoice/bill/credit note/debit note, incoming order/outgoing order/internal transfer reports. When you print a report it automatically merges those PDF attachments with that report. You can merge additional PDF attachments like terms and conditions, privacy policy, return policy, copyright, after sales service, support service etc with the report.""",
    'sequence':
    10,
    'depends': ['account'],
    'data': [
        'sh_inv_merge_pdf/views/res_config_settings_views.xml',
        'sh_inv_merge_pdf/views/account_move_views.xml',
    ],
    'demo': [],
    'installable':
    True,
    'application':
    True,
    'auto_install':
    False,
    "license":
    "OPL-1",
    "images": ["static/description/background.png", ],
    "price": "150",
    "currency": "EUR"
}
