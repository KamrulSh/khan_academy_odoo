from odoo import models, fields

class AcademyCourse(models.Model):
    _name = 'khanacademy.course'
    _description = 'Here Course information is stored.'

    course_name = fields.Char(string='Course Name')
    course_code = fields.Char(string='Course Code')
    course_description = fields.Text(string='Course Description')
    credit_hour = fields.Integer(string='Credit')
