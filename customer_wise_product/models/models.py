# -*- coding: utf-8 -*-

from odoo import models, fields, api


class InheritProduct(models.Model):
    _inherit = 'product.product'

    customer_ids = fields.Many2many('res.partner', string="Customers")

    def name_get(self):
        result = []
        if self.env.context.get('partner_id'):
            partner_id = self.env.context.get('partner_id')
            products = self.env['product.product'].search([('customer_ids', '=', partner_id)])
            if len(products.ids) > 0:
                for product in products:
                    name = '%s' % product.name
                    result.append((product.id, name))
                return result
            else:
                return self.get_normal_result()
        else:
            return self.get_normal_result()

    def get_normal_result(self):
        result = []
        for product in self:
            name = '%s' % product.name
            result.append((product.id, name))
        return result
