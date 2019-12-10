// Copyright (c) 2019, Parth - M20Zero and contributors
// For license information, please see license.txt

frappe.ui.form.on("Membership Plan",{
	onload: function(frm,cdt,cdn) {
		var membership_plan = frappe.model.get_doc(cdt, cdn);
		frappe.call({
			method:"membershipmanagement.members.doctype.membership_plan.membership_plan.get_plan_benefit",
			callback: function(r){
				var i;
				for (i = 0; i < r.message.length; i++) {
					var child = cur_frm.add_child("plan_benefit")
					frappe.model.set_value(child.doctype, child.name, "plan_benefit_name", r.message[i])
					refresh_field("plan_benefit")	
				} 
			}
		});		
	}
});
