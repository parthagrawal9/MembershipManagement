# -*- coding: utf-8 -*-
# Copyright (c) 2019, Parth - M20Zero and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
import frappe.utils
from datetime import date
from frappe import _
from frappe.model.document import Document

class Member(Document):
	def validate(self):
		# set Missing Names
		self.full_name = get_full_name(self.member)
		self.plan_price = get_plan_price(self.plan)
		self.total = get_total(self.plan_price,self.duration)
			
@frappe.whitelist()
def get_full_name(member):
	user = frappe.get_doc("User",member)
	return " ".join(filter(None,[user.first_name,user.middle_name,user.last_name]))

@frappe.whitelist()
def get_total(plan_price, duration):
	return float(plan_price)*float(duration)

@frappe.whitelist()
def get_plan_price(plan):
	planDetail = frappe.get_doc("Membership Plan",plan)
	return planDetail.price