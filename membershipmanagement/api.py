import frappe
from frappe import _
from frappe.model.document import Document
from frappe.utils import date_diff, nowdate

def new_member(doc,method):
    send_welcome_email(doc,method)
    add_balance_log(doc,method)

def send_welcome_email(doc,method):
    msg = " ".join([
        'Welcome to Membership Management System <b>',doc.full_name, 
        '<br>Plan:</b> ', doc.plan, 
        '<br><b>Start Date:</b> ',doc.joining_date, 
        '<br><b>End Date:</b> ',doc.end_date,
        '<br><b>Balance:</b> ',str(doc.balance)
        ])
    frappe.sendmail(
        recipients=[doc.member],
        sender=frappe.session.user,
        subject="New Membership",
        message=msg,
        now=True
    )
    frappe.msgprint(_("Welcome Email Sent!"))

def add_balance_log(doc,method):
    # doc = frappe.get_doc('Member', doc.member)
    doc.append('balance_log', {
        'date': doc.joining_date,
        'description': ' ' . join(['Membership - ',doc.plan, ' - ', doc.duration, ' month/s']),
        'amount': doc.total,
        'balance': (doc.balance - doc.total)
    })
    doc.save()

# def get_plan_benefit(doc,method):
#     plan = frappe.get_all('Benefit', fields=['title', 'description'])
#     for plan in plan:
#         doc.append('plan_benefit', {
#         'plan_benefit_name': plan.title
#     })
#     doc.save()





