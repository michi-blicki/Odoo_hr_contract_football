# -*- coding: utf-8 -*-

from dateutil.relativedelta import relativedelta

from odoo import _, api, fields, models
from odoo.exceptions import ValidationError


class HrContract(models.Model):
	_inherit = "hr.contract"

	contract_runtime = fields.Float(string="Contract Runtime (years)")
	contract_optional_extension = fields.Float(string="Contract Optional Extension (years)")
	signing_fee = fields.Monetary(string="Signing Fee", currency_field="currency_id")
	signing_fee_pay_date = fields.Date(string="Signing Fee Pay Date")
	transfer_type = fields.Selection(
		selection=[
			("purchase", "Purchase"),
			("free_transfer", "Free Transfer"),
			("loan", "Loan"),
		],
		string="Transfer Type",
	)
	termination_clause_type = fields.Selection(
		selection=[
			("fixed", "Fixed"),
			("variable", "Variable"),
		],
		string="Termination Clause Type",
	)
	termination_amount = fields.Monetary(string="Termination Amount", currency_field="currency_id")
	
	loyalty_bonus = fields.Monetary(string="Loyalty Bonus", currency_field="currency_id")
	loyalty_bonus_pay_date = fields.Date(string="Loyalty Bonus Pay Date")
	game_appearance_bonus = fields.Monetary(string="Game Appearance Bonus", currency_field="currency_id")
	game_playtime_bonus = fields.Monetary(string="Game Playtime Bonus (minutes)", currency_field="currency_id")
	training_appearance_bonus = fields.Monetary(string="Training Appearance Bonus", currency_field="currency_id")
	training_traintime_bonus = fields.Monetary(string="Training Traintime Bonus (minutes)", currency_field="currency_id")
	goal_bonus = fields.Monetary(string="Goal Bonus", currency_field="currency_id")
	clean_sheet_bonus = fields.Monetary(string="Clean Sheet Bonus", currency_field="currency_id")
	red_card_penalty = fields.Monetary(string="Red Card Penalty (each)", currency_field="currency_id")
	yellow_card_penalty = fields.Monetary(string="Yellow Card Penalty (each)", currency_field="currency_id")
	team_success_bonus = fields.Monetary(string="Team Success Bonus", currency_field="currency_id")
	release_clause_amount = fields.Monetary(string="Release Clause Amount", currency_field="currency_id")
	buyout_clause_amount = fields.Monetary(string="Buyout Clause Amount", currency_field="currency_id")
	loan_conditions = fields.Text(string="Loan Conditions")
	sponsorship_bonus = fields.Monetary(string="Sponsorship Bonus", currency_field="currency_id")
	trainer_title_bonus = fields.Monetary(string="Trainer Title Bonus", currency_field="currency_id")
	trainer_position_bonus = fields.Monetary(string="Trainer Position Bonus", currency_field="currency_id")
	trainer_retention_bonus = fields.Monetary(string="Trainer Retention Bonus", currency_field="currency_id")

	termination_variable_condition = fields.Many2one(
		comodel_name="hr.contract.football.condition", 
		domain="[('type', '=', 'termination_variable')]", 
		string="Termination Variable Condition"
	)
	termination_variable_condition_custom = fields.Html(string="Termination Variable Condition Custom Text")
	loan_return_conditions = fields.Many2one(
		comodel_name="hr.contract.football.condition", 
		domain="[('type', '=', 'loan_return')]", 
		string="Loan Return Conditions"
	)
	loan_return_conditions_custom = fields.Html(string="Loan Return Custom Conditions")
	sponsorship_conditions = fields.Many2one(
		comodel_name="hr.contract.football.condition", 
		domain="[('type', '=', 'sponsorship')]", 
		string="Sponsorship Conditions"
	)
	sponsorship_conditions_custom = fields.Html(string="Sponsorship Custom Conditions")
	trainer_position_condition = fields.Many2one(
		comodel_name="hr.contract.football.condition",
		domain="[('type', '=', 'trainer_position')]",
		string="Trainer Position Condition"
	)
	trainer_position_condition_custom = fields.Html(string="Trainer Position Custom Conditions")
	trainer_title_condition = fields.Many2one(
		comodel_name="hr.contract.football.condition",
		domain="[('type', '=', 'trainer_title')]",
		string="Trainer Title Condition"
	)
	trainer_title_condition_custom = fields.Html(string="Trainer Title Custom Conditions")
	trainer_retention_condition = fields.Many2one(
		comodel_name="hr.contract.football.condition",
		domain="[('type', '=', 'trainer_retention')]",
		string="Trainer Retention Condition"
	)
	trainer_retention_condition_custom = fields.Html(string="Trainer Retention Custom Conditions")
	trainer_side_jobs_conditions = fields.Many2one(
		comodel_name="hr.contract.football.condition",
		domain="[('type', '=', 'trainer_side_jobs')]",
		string="Trainer Side Jobs Conditions"
	)
	trainer_side_jobs_conditions_custom = fields.Html(string="Trainer Side Jobs Custom Conditions")

	@api.model
	def _compute_runtime_end_date(self, date_start, contract_runtime):
		if not date_start or contract_runtime in (None, False):
			return False
		start_date = fields.Date.to_date(date_start)
		months = int(round(contract_runtime * 12))
		return start_date + relativedelta(months=months)

	@api.onchange("date_start", "contract_runtime")
	def _onchange_contract_runtime_date_end(self):
		for contract in self:
			if contract.date_start and contract.contract_runtime not in (None, False):
				contract.date_end = contract._compute_runtime_end_date(
					contract.date_start,
					contract.contract_runtime,
				)

	@api.model_create_multi
	def create(self, vals_list):
		for vals in vals_list:
			date_start = vals.get("date_start")
			contract_runtime = vals.get("contract_runtime")
			if date_start and contract_runtime not in (None, False):
				vals["date_end"] = self._compute_runtime_end_date(date_start, contract_runtime)
		return super().create(vals_list)

	def write(self, vals):
		res = super().write(vals)
		if "date_start" in vals or "contract_runtime" in vals:
			for contract in self:
				if contract.date_start and contract.contract_runtime not in (None, False):
					computed_date_end = contract._compute_runtime_end_date(
						contract.date_start,
						contract.contract_runtime,
					)
					if contract.date_end != computed_date_end:
						super(HrContract, contract).write({"date_end": computed_date_end})
		return res

	@api.constrains(
		"signing_fee",
		"termination_amount",
		"loyalty_bonus",
		"game_appearance_bonus",
		"goal_bonus",
		"clean_sheet_bonus",
		"team_success_bonus",
		"release_clause_amount",
		"buyout_clause_amount",
		"sponsorship_bonus",
		"trainer_title_bonus",
		"trainer_position_bonus",
		"trainer_retention_bonus",
	)
	def _check_non_negative_monetary_fields(self):
		monetary_fields = [
			"signing_fee",
			"termination_amount",
			"loyalty_bonus",
			"game_appearance_bonus",
			"goal_bonus",
			"clean_sheet_bonus",
			"team_success_bonus",
			"release_clause_amount",
			"buyout_clause_amount",
			"sponsorship_bonus",
			"trainer_title_bonus",
			"trainer_position_bonus",
			"trainer_retention_bonus",
		]
		for contract in self:
			for field_name in monetary_fields:
				if contract[field_name] is not None and contract[field_name] < 0:
					field_label = contract._fields[field_name].string
					raise ValidationError(
						_("The field '%s' must be zero or greater.") % field_label
					)

	@api.constrains("signing_fee", "signing_fee_pay_date", "loyalty_bonus", "loyalty_bonus_pay_date")
	def _check_required_bonus_pay_dates(self):
		for contract in self:
			if contract.signing_fee and contract.signing_fee > 0 and not contract.signing_fee_pay_date:
				raise ValidationError(
					_("Signing Fee Pay Date is required when Signing Fee is greater than zero.")
				)
			if contract.loyalty_bonus and contract.loyalty_bonus > 0 and not contract.loyalty_bonus_pay_date:
				raise ValidationError(
					_("Loyalty Bonus Pay Date is required when Loyalty Bonus is greater than zero.")
				)

	@api.onchange('termination_variable_condition')
	def _onchange_termination_variable_condition(self):
		for contract in self:
			if contract.termination_variable_condition:
				contract.termination_variable_condition_custom = contract.termination_variable_condition.text
			else:
				contract.termination_variable_condition_custom = False

	@api.onchange('loan_return_conditions')
	def _onchange_loan_return_conditions(self):
		for contract in self:
			if contract.loan_return_conditions:
				contract.loan_return_conditions_custom = contract.loan_return_conditions.text
			else:
				contract.loan_return_conditions_custom = False

	@api.onchange('sponsorship_conditions')
	def _onchange_sponsorship_conditions(self):
		for contract in self:
			if contract.sponsorship_conditions:
				contract.sponsorship_conditions_custom = contract.sponsorship_conditions.text
			else:
				contract.sponsorship_conditions_custom = False
	
	@api.onchange('trainer_position_condition')
	def _onchange_trainer_position_condition(self):
		for contract in self:
			if contract.trainer_position_condition:
				contract.trainer_position_condition_custom = contract.trainer_position_condition.text
			else:
				contract.trainer_position_condition_custom = False

	@api.onchange('trainer_title_condition')
	def _onchange_trainer_title_condition(self):
		for contract in self:
			if contract.trainer_title_condition:
				contract.trainer_title_condition_custom = contract.trainer_title_condition.text
			else:
				contract.trainer_title_condition_custom = False

	@api.onchange('trainer_retention_condition')
	def _onchange_trainer_retention_condition(self):
		for contract in self:
			if contract.trainer_retention_condition:
				contract.trainer_retention_condition_custom = contract.trainer_retention_condition.text
			else:
				contract.trainer_retention_condition_custom = False

	@api.onchange('trainer_side_jobs_conditions')
	def _onchange_trainer_side_jobs_conditions(self):
		for contract in self:
			if contract.trainer_side_jobs_conditions:
				contract.trainer_side_jobs_conditions_custom = contract.trainer_side_jobs_conditions.text
			else:
				contract.trainer_side_jobs_conditions_custom = False