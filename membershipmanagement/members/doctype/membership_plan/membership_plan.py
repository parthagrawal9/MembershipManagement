# -*- coding: utf-8 -*-
# Copyright (c) 2019, Parth - M20Zero and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
# import frappe.utils
# from datetime import date
from frappe import _
from frappe.model.document import Document


class MembershipPlan(Document):
	pass

@frappe.whitelist()
def get_plan_benefit():
	plan = frappe.get_all('Benefit', fields=['title', 'description'])
	data = []
	for value in plan:
		data.append(value.title)
	return data