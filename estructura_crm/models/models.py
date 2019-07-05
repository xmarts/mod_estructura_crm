# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ResPartner(models.Model):
	_inherit = "res.partner"

	company_type = fields.Selection([('person','Persona Fisica'),('company','Persona Moral')])

# class estructura_crm(models.Model):
#     _name = 'estructura_crm.estructura_crm'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100