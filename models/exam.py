from odoo import fields, models

class AcademyExam(models.Model):
    _name = 'khanacademy.exam'
    _description = 'Exam information.'

    name = fields.Char(string='Exam Name')
    exam_id = fields.Char(string='Exam ID')
    student_count = fields.Char(string='Student Count')
    invigilator = fields.Char(string='Invigilator Name')
    exam_date = fields.Date(string='Exam Date')
