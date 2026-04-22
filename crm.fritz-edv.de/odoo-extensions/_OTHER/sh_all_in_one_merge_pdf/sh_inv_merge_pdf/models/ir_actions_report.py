# -*- coding: utf-8 -*-
# Part of Softhealer Technologies.
from PyPDF2 import PdfFileWriter, PdfFileReader
from odoo import models
import io
import base64


class IrActionsReport(models.Model):
    _inherit = 'ir.actions.report'

    def _render_qweb_pdf(self, report_ref, res_ids=None, data=None):

        res = super(IrActionsReport, self)._render_qweb_pdf(
            report_ref, res_ids=res_ids, data=data)
        
        if not data:
            data = {'report_type': 'pdf'}
            # report_ref = report_ref.report_name
        if data:
            if data.get('report_type') == 'pdf' and res_ids and len(res_ids) == 1:

                report_sudo = self._get_report(report_ref)
                if report_sudo.model == 'account.move' and report_sudo.id in self.env.company.sudo().sh_inv_merge_pdf_report_ids.ids and self.env.company.sudo().sh_inv_merge_pdf_report_bool:

                    record = self.env['account.move'].browse(res_ids)

                    if record and record.sh_inv_merge_pdf_attachment_ids and record.sh_inv_merge_pdf_attachment_bool:
                        writer = PdfFileWriter()
                        pdf_content = [res[0]]
                        for attachment in record.sh_inv_merge_pdf_attachment_ids:
                            datas = base64.b64decode(
                                attachment.with_context(bin_size=False).datas)
                            pdf_content.append(datas)
                        for document in pdf_content:
                            reader = PdfFileReader(
                                io.BytesIO(document), strict=False)
                            for page in range(0, reader.getNumPages()):
                                writer.addPage(reader.getPage(page))
                        with io.BytesIO() as _buffer:
                            writer.write(_buffer)
                            merged_pdf = _buffer.getvalue()
                            _buffer.close()
                            return merged_pdf, 'pdf'

        return res
