# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError

class ResPartner(models.Model):
	_inherit = "res.partner"

	company_type = fields.Selection([('person','Persona Fisica'),('company','Persona Moral')])
	
class AddDateCrm(models.Model):
	_inherit = "crm.lead"

	date_now = fields.Datetime(string="Fecha de lead")
	partner_address_mobile = fields.Char('Partner Contact Mobile', related='partner_id.mobile', readonly=True)
	phone = fields.Char('Phone', track_visibility='onchange', track_sequence=5)
	mobile = fields.Char('Móvil', track_visibility='onchange')
