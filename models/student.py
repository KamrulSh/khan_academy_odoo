from odoo import fields, models, api
import re
from odoo.exceptions import ValidationError
class AcademyStudent(models.Model):
    _name = 'khanacademy.student'
    _description = 'Student information.'

    name = fields.Char(string='Student Name')
    student_id = fields.Char(string='Student ID')
    student_phone = fields.Char(string='Phone Number')
    student_email = fields.Char(string='Email Address')
    student_photo = fields.Binary(string="Photo", attachment=True)
    student_dob = fields.Date(string="Date of Birth")

    course_ids = fields.Many2many('khanacademy.course', string='Courses')
    department_id = fields.Many2one('khanacademy.department', string='Department')

    # email address validation    
    @api.onchange('student_email')
    def validate_mail(self):
        if self.student_email:
            match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', self.student_email)
            if match == None:
                raise ValidationError('Not a valid E-mail ID')