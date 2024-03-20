# Copyright (c) 2024, Frappe Technologies Pvt. Ltd. and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class TemporaryAccountDetails(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.model.document import Document
		from frappe.types import DF

		custom_course: DF.Data | None
		custom_course_1: DF.Data | None
		custom_start_year: DF.Date | None
		just1: DF.Table[Document]
	# end: auto-generated types
	pass
