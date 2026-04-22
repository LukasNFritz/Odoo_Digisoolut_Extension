# -*- coding: utf-8 -*-
# Part of Softhealer Technologies.
from odoo import fields, models


class ResConfigSetting(models.TransientModel):
    _inherit = 'res.config.settings'

    sh_inv_merge_pdf_report_bool = fields.Boolean(string="Invoice Merge Pdf Reports",
                                                    related="company_id.sh_inv_merge_pdf_report_bool",
                                                    readonly=False)
    sh_inv_merge_pdf_attachment_bool = fields.Boolean(string="Invoice merge attachment to reports",
                                                    related="company_id.sh_inv_merge_pdf_attachment_bool",
                                                    readonly=False)
    sh_inv_merge_pdf_report_ids = fields.Many2many(
        related="company_id.sh_inv_merge_pdf_report_ids",
        readonly=False,
        domain="[('model', '=', 'account.move'),('report_type','=','qweb-pdf')]",
        string="Invoice Reports")
