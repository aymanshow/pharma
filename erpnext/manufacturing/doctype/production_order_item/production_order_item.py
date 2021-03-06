# -*- coding: utf-8 -*-
# Copyright (c) 2015, Revaluesoft S.A.E
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class ProductionOrderItem(Document):
	pass

def on_doctype_update():
	frappe.db.add_index("Production Order Item", ["item_code", "source_warehouse"])