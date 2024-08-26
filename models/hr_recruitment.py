from odoo import models, fields, api, SUPERUSER_ID

class HrApplicantRefuseReason(models.Model):
    _inherit = 'hr.applicant.refuse.reason'

    template_id = fields.Many2one('mail.template', string="Email Template")

    @api.model
    def remove_default_reasons(self):
        reasons_to_delete = [
            "Doesn't fit the job requirements",
            "Refused by Applicant: don't like job",
            "Refused by Applicant: better offer",
            "Language issues",
            "Role already fulfilled",
            "Duplicate",
            "Spam",
            "Refused by Applicant: salary"
        ]
        ir_model_data = self.env['ir.model.data']
        for reason_name in reasons_to_delete:
            reason_data = ir_model_data.search(
                [('model', '=', 'hr.applicant.refuse.reason'), ('name', '=', reason_name)])
            if reason_data:
                reason_data.unlink()