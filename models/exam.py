from odoo import fields, models

class AcademyExam(models.Model):
    _name = 'khanacademy.exam'
    _description = 'Exam information.'

    exam_id = fields.Char(string='Exam ID')
    student_count = fields.Char(string='Student Count')
    exam_date = fields.Date(string='Exam Date')

    name = fields.Many2one('khanacademy.course', string='Course/Exam Name')
    invigilator = fields.Many2one('khanacademy.teacher', string='Invigilator Name')