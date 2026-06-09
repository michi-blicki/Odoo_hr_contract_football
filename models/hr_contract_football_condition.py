# -*- coding: utf-8 -*-

from odoo import _, api, fields, models
from odoo.exceptions import ValidationError

class HrContractFootballCondition(models.Model):
    _name = "hr.contract.football.condition"
    _description = "Football Contract Condition"

    name = fields.Char(string="Condition Name", required=True)
    type = fields.Selection(
        selection=[
            ("termination_variable", "Termination Variable Condition"),
            ("loan_return", "Loan Return Condition"),
            ("sponsorship", "Sponsorship Condition"),
            ("trainer_position", "Trainer Position Condition"),
            ("trainer_title", "Trainer Title Condition"),
            ("trainer_retention", "Trainer Retention Condition"),
            ("trainer_side_jobs", "Trainer Side Jobs Condition"),
        ],
        string="Condition Type",
        required=True,
    )
    text = fields.Html(string="Condition Text", required=True)
    sequence = fields.Integer(string="Sequence", default=10)
    active = fields.Boolean(string="Active", default=True)