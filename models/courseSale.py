from odoo import models, fields


class CourseSale(models.Model):
    _inherit = 'product.template'
    _description = 'Course Add'

    name = fields.Char(string="Course Name")
    price = fields.Float(string="Price")
    image = fields.Binary(string='Photo', attachment=True)