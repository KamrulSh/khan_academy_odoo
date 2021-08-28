from odoo import fields, models

class AcademyStudent(models.Model):
    _name = 'khanacademy.student'
    _description = 'Student information.'

    student_name = fields.Char(string='Student Name')
    student_id = fields.Char(string='Student ID')
    student_phone = fields.Char(string='Phone Number')
    student_email = fields.Char(string='Email Address')
    student_photo = fields.Binary(string="Photo", attachment=True)
    student_dob = fields.Date(string="Date of Birth")