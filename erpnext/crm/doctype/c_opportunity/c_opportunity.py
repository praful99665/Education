# Copyright (c) 2024, Frappe Technologies Pvt. Ltd. and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class C_opportunity(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from education.education.doctype.program_enrollment_course.program_enrollment_course import ProgramEnrollmentCourse
		from frappe.types import DF

		address: DF.Data | None
		city: DF.Data | None
		course: DF.Table[ProgramEnrollmentCourse]
		course_fee: DF.Data | None
		d_name: DF.Data | None
		email: DF.Data | None
		first_name: DF.Data | None
		full_name: DF.Data | None
		gender: DF.Literal["Male", "Female", "Other"]
		last_name: DF.Data | None
		lead_id: DF.Link | None
		middle_name: DF.Data | None
		mob: DF.Data | None
		payment_amount: DF.Data | None
		source: DF.Data | None
		status: DF.Literal["LEAD", "OPPORTUNITY", "CONVERTED", "LOST"]
	# end: auto-generated types
	pass
