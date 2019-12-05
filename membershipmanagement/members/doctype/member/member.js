// Copyright (c) 2019, Parth - M20Zero and contributors
// For license information, please see license.txt

cur_frm.toggle_display("end_date", true);
frappe.ui.form.on('Member', {
	member: function(frm, cdt, cdn){
		var member = frappe.model.get_doc(cdt, cdn);
		if(member.member){
			frappe.call({
				method:"membershipmanagement.members.doctype.member.member.get_full_name",
				args:{
					member: member.member
				},
				callback: function(r){
					frappe.model.set_value(cdt, cdn, "full_name",r.message)
				}
			});	
		}else{
			frappe.model.set_value(cdt, cdn, "full_name",null);
		}
	}

});

frappe.ui.form.on('Member', {
	plan: function(frm, cdt, cdn){
		var member = frappe.model.get_doc(cdt, cdn);
		if(member.plan){
			frappe.call({
				method:"membershipmanagement.members.doctype.member.member.get_plan_price",
				args:{
					plan: member.plan
				},
				callback: function(r){
					frappe.model.set_value(cdt, cdn, "plan_price",r.message)
				}
			});
		}else{
			frappe.model.set_value(cdt, cdn, "plan_price",null);
		}
	}

});

frappe.ui.form.on('Member', {
	plan: function(frm, cdt, cdn){
		var member = frappe.model.get_doc(cdt, cdn);
		if(member.plan){
			frappe.call({
				method:"membershipmanagement.members.doctype.member.member.get_total",
				args:{
					plan_price: member.plan_price,
					duration: member.duration
				},
				callback: function(r){
					frappe.model.set_value(cdt, cdn, "total",r.message)
				}
			});
		}else{
			frappe.model.set_value(cdt, cdn, "total",null);
		}
	} 
});

frappe.ui.form.on('Member', {
	duration: function(frm, cdt, cdn){
		var member = frappe.model.get_doc(cdt, cdn);
		if(member.plan){
			frappe.call({
				method:"membershipmanagement.members.doctype.member.member.get_total",
				args:{
					plan_price: member.plan_price,
					duration: member.duration
				},
				callback: function(r){
					frappe.model.set_value(cdt, cdn, "total",r.message)
				}
			});
		}else{
			frappe.model.set_value(cdt, cdn, "total",null);
		}
		frappe.model.set_value(cdt, cdn, "end_date", frappe.datetime.add_months(member.joining_date, member.duration));
	} 
});

frappe.ui.form.on("Member", {
	joining_date: function(frm, cdt, cdn){
		var member = frappe.model.get_doc(cdt, cdn);
		frappe.model.set_value(cdt, cdn, "end_date", frappe.datetime.add_months(member.joining_date, member.duration));
	} 
});

frappe.ui.form.on("Member", {
	duration: function(frm, cdt, cdn){
		var member = frappe.model.get_doc(cdt, cdn);
		frappe.model.set_value(cdt, cdn, "balance_log.date", member.joining_date);
		frappe.model.set_value(cdt, cdn, "balance_log.bal", (member.balance-member.total));
		frappe.model.set_value(cdt, cdn, "balance_log.description", "welcome");
		frappe.model.set_value(cdt, cdn, "balance_log.amount", meber.total);
	} 

	
});