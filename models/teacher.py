from odoo import fields, models

class AcademyTeacher(models.Model):
    _name = 'khanacademy.teacher'
    _description = 'Teacher information.'

    name = fields.Char(string='Teacher Name')
    teacher_id = fields.Char(string='Teacher ID')
    teacher_phone = fields.Char(string='Phone Number')
    teacher_email = fields.Char(string='Email Address')
    teacher_photo = fields.Binary(string="Photo", attachment=True)

    course_ids = fields.Many2many('khanacademy.course',string='Courses')
    department_id = fields.Many2one('khanacademy.department', string='Department')