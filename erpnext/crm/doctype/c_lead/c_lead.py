# Copyright (c) 2024, Frappe Technologies Pvt. Ltd. and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class C_Lead(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		address: DF.Data | None
		city: DF.Data | None
		district: DF.Data | None
		doc_name: DF.Data | None
		email: DF.Data
		first_name: DF.Data | None
		full_name: DF.Data | None
		gender: DF.Literal["----Select----", "Male", "Female", "Other"]
		last_name: DF.Data | None
		middle_name: DF.Data | None
		mob: DF.Data | None
		sourse: DF.Link | None
		status: DF.Literal["LEAD", "OPPORTUNITY", "CONVERTED", "LOST"]
		whatsapp: DF.Data | None
	# end: auto-generated types
	pass
