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
        '<br><b>Balance:</b> ',str(doc.balance),
        '<br><b>Status:</b ',doc.status
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
        print('1')
        if doc.status == 'Accepted':
            print('2')
            user = frappe.new_doc('User')
            # print(doc)
            # print(user)
            # print(type(doc.email))
            user.email = doc.email
            user.first_name = doc.full_name
            user.save()

        # print('Current : ',doc.status)
        # print('Previous : ',doc.prev_status)
        print('3')
        doc.prev_status = doc.status
        doc.save()
        # print('Previous : ',doc.prev_status)
        print('4')
        email_queue_send_now()

def email_queue_send_now():
    data = frappe.get_list('Email Queue', filters={'Status': 'Not Sent'})
    for email in data:
        frappe.email.doctype.email_queue.email_queue.send_now(email.name)
