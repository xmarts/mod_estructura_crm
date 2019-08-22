# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError

class ResPartner(models.Model):
	_inherit = "res.partner"

	company_type = fields.Selection([('person','Persona Fisica'),('company','Persona Moral')])

class CrmLead(models.Model):
	_inherit = "crm.lead"

	partner_name = fields.Many2one('res.partner', "Customer Name", track_visibility='onchange', track_sequence=2, index=True, help='The name of the future partner company that will be created while converting the lead into opportunity')	