from odoo import fields, models

class AcademyDepartment(models.Model):
    _name = 'khanacademy.department'
    _description = 'Department Information'

    name = fields.Char(string='Department Name')
    budget = fields.Float(string='Department Budget')

    engr_dept = fields.Boolean(string='Engineering Department')

    teacher_ids = fields.One2many('khanacademy.teacher', 'department_id', string='Teacher List')
    student_ids = fields.One2many('khanacademy.student', 'department_id', string='Student List')
    course_ids = fields.One2many('khanacademy.course', 'department_id', string='Course List')