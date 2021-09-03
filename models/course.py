from odoo import models, fields

class AcademyCourse(models.Model):
    _name = 'khanacademy.course'
    _description = 'Here Course information is stored.'

    name = fields.Char(string='Course Name')
    course_code = fields.Char(string='Course Code')
    course_description = fields.Text(string='Course Description')
    credit_hour = fields.Integer(string='Credit')

    teacher_id = fields.Many2one('khanacademy.teacher', string='Course Teacher')
    department_id = fields.Many2one('khanacademy.department', string='Department')