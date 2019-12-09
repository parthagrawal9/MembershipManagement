from __future__ import unicode_literals
import frappe
from frappe.utils import date_diff, nowdate, format_date, add_days

def daily():
    member = frappe.get_all('Member', fields=['member', 'end_date','plan','joining_date','full_name'])
    for member in member:
        if (date_diff(member.end_date,nowdate())) == 2:
            send_membership_renewal_mail(member)

def send_membership_renewal_mail(member):
    msg = " ".join([
        '<b>REMINDER!!! </b> Membership Renewal : <b>',member.full_name, 
        '<br>Plan:</b> ', member.plan, 
        '<br><b>Start Date:</b> ',member.joining_date, 
        '<br><b>End Date:</b> ',member.end_date,
        ])
    frappe.sendmail(
        recipients=[member.member],
        sender=frappe.session.user,
        subject="Membership Renewal",
        message=msg,
        now=True
    )