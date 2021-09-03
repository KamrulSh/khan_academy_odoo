from odoo.exceptions import ValidationError
import re
from odoo import api, fields, models

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

    # email address validation    
    @api.onchange('teacher_email')
    def validate_mail(self):
        if self.teacher_email:
            match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', self.teacher_email)
            if match == None:
                raise ValidationError('Not a valid E-mail ID')