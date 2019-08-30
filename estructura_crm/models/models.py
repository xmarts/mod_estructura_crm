# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError

class ResPartner(models.Model):
	_inherit = "res.partner"

	company_type = fields.Selection([('person','Persona Fisica'),('company','Persona Moral')])
	
	'''nombre_comercial = fields.Char()	'''