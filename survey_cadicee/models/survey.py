from odoo import _, api, models, fields


class SurveyQuestion(models.Model):
    _inherit = "survey.question"

    question = fields.Html('Question Name', required=True, translate=True)
