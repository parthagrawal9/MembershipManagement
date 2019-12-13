from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
			"label": _("Members"),
            		"icon": "octicon octicon-briefcase",
			"items":[
					{
						"type": "doctype",
						"name": "Member",
                    				"label": _("Members"),
						"description": _("Membership Management")
					},
					{
						"type": "doctype",
						"name": "Membership Plan",
                    				"label": _("Membership Plan"),
						"description": _("Membership Management")
					},
					{
						"type": "doctype",
						"name": "Benefit",
                    				"label": _("Benefit"),
						"description": _("Membership Management")
					},
					{
						"type": "doctype",
						"name": "Member Request",
                    				"label": _("Member Request"),
						"description": _("Membership Management")
					}

     			       ]
    		 }
    		]
