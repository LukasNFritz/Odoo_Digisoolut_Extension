# -*- coding: utf-8 -*-
# Part of Softhealer Technologies.
from odoo import fields, models


class AccountMove(models.Model):
    _inherit = "account.move"

    sh_inv_merge_pdf_attachment_bool = fields.Boolean(string="Merge attachment to reports",
                                                    related="company_id.sh_inv_merge_pdf_attachment_bool",
                                                    readonly=False)
    sh_inv_merge_pdf_attachment_ids = fields.Many2many(
        comodel_name="ir.attachment",
        string="Attachment Merge",
        relation="rel_sh_inv_merge_attachment_id")
