import frappe
from frappe import _
from frappe.model.document import Document
from frappe.utils import date_diff, nowdate,datetime
import membershipmanagement.members.doctype.member.member as membershipmanagement

def new_member(doc,method):
    send_welcome_email(doc,method)
    add_balance_log(doc,method)

def send_welcome_email(doc,method):
    print('hi')
    # msg = " ".join([
    #     'Welcome to Membership Management System <b>',doc.full_name,
    #     '<br>Plan:</b> ', doc.plan, 
    #     '<br><b>Start Date:</b> ',doc.joining_date, 
    #     '<br><b>End Date:</b> ',doc.end_date,
    #     '<br><b>Balance:</b> ',str(doc.balance)
    #     ])
    # frappe.sendmail(
    #     recipients=[doc.member],
    #     sender=frappe.session.user,
    #     subject="New Membership",
    #     message=msg,
    #     now=True
    # )
    # frappe.msgprint(_("Welcome Email Sent!"))

def add_balance_log(doc,method):
    # doc = frappe.get_doc('Member', doc.member)
    doc.append('balance_log', {
        'date': doc.joining_date,
        'description': ' ' . join(['Membership - ',doc.plan, ' - ', doc.duration, ' month/s']),
        'amount': doc.total,
        'balance': (doc.balance - doc.total)
    })
    doc.save()

def new_membership_request(doc,method):
    msg = " ".join([
        'Dear <b>',doc.full_name,
        '</b><br>Welcome to Membership Management System <b>', 
        '</b><br>Your Membership Application is sent for approval. Kindly wait for further pdates.',
        '<br><b>Plan:</b> ', doc.plan,
        '<br><b>Duration:</b> ', doc.duration, 
        '<br><b>Status: </b> Pending'
        ])
    frappe.sendmail(
        recipients=[doc.email],
        sender='agrawal.parth9@gmail.com',
        subject="New Membership : Pending Approval",
        message=msg,
        now=True
    )
    frappe.msgprint(_("Please check your email"))

def membership_state_change(doc,method):
    if doc.status != doc.prev_status:
        if doc.status == 'Accepted':
            add_new_user(doc,method)
            add_new_member(doc,method)
        
        doc.prev_status = doc.status
        doc.save()

        email_queue_send_now()

def add_new_member(doc,method):
    member = frappe.new_doc('Member')
    member.member = doc.email
    member.full_name = doc.full_name
    member.balance = 50000
    member.joining_date = nowdate()
    member.end_date = frappe.utils.data.add_months(member.joining_date, int(doc.duration))
    member.plan = doc.plan
    member.duration = doc.duration
    member.plan_price = membershipmanagement.get_plan_price(doc.plan)
    member.total = membershipmanagement.get_total(member.plan_price,member.duration)
    member.save()

def add_new_user(doc,method):
    user = frappe.new_doc('User')
    user.email = doc.email
    user.first_name = doc.full_name
    user.save()

def email_queue_send_now():
    data = frappe.get_list('Email Queue', filters={'Status': 'Not Sent'})
    for email in data:
        frappe.email.doctype.email_queue.email_queue.send_now(email.name)
