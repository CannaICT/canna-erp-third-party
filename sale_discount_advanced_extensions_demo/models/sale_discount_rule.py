# Copyright (C) 2019 Noviat nv/sa (www.noviat.com).
# Copyright (C) 2020-TODAY Serpent Consulting Services Pvt. Ltd. (<http://www.serpentcs.com>).
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import api, models


class SaleDiscountRule(models.Model):
    _inherit = "sale.discount.rule"

    @api.model
    def _selection_matching_type(self):
        res = super(SaleDiscountRule, self)._selection_matching_type()
        return res + [("pallet", "Pallet")]

    @api.model
    def _selection_matching_extra(self):
        res = super(SaleDiscountRule, self)._selection_matching_extra()
        return res + [("extra", "Extra")]

    def _matching_type_methods(self):
        methods = super(SaleDiscountRule, self)._matching_type_methods()
        methods["pallet"] = "_pallet_matching"
        return methods

    def _matching_extra_methods(self):
        methods = super(SaleDiscountRule, self)._matching_extra_methods()
        methods["extra"] = "_extra_matching"
        return methods

    def _pallet_matching(self, lines):
        _logger.warn("_pallet_matching for rule %s, lines=%s", self, lines)
        return True

    def _extra_matching(self, lines):
        _logger.warn("_extra_matching for rule %s, lines=%s", self, lines)
        return True
