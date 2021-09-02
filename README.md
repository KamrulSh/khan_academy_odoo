# khan-academy-odoo

Created an academy module where there are 5 menus for Departments, Students, Teachers, Courses, Exams.
Each menu have different views (Tree, Form, search).

## 0. Departments model & view:

Here all the departments information will show and there is an option for creating new department information.
One2many: One department have many teachers, students and courses.
View all the information when clicking on the specific data.

![Departments1](./picture/9.png)
![Departments2](./picture/10.png)
![Departments3](./picture/11.png)

## 1. Students model & view:

Here all the students information will show and there is an option for creating new student information.
Many2one: student model with department --> One department has multiple students
Many2many: student model with course --> One course has multiple students and one student can take multiple courses.

![Student1](./picture/12.png)
![Student2](./picture/13.png)

## 2. Courses model & view:

Here all the courses information will show and there is an option for creating new course information.
Many2one: course model with department --> One department has multiple courses
course model with teacher --> One teacher can take multiple courses

![Course1](./picture/14.png)

## 3. Teachers model & view:

Here all the teachers information will show and there is an option for creating new teacher information.
Many2one: teacher model with department --> One department has multiple teachers
Many2many: teacher model with course --> one teacher can take multiple courses.

![Teachers1](./picture/15.png)

## 4. Exams model & view:

Here all the exams information will show and there is an option for creating new exam information.
Many2one: exam model with course --> One course has multiple exams
exam model with teacher --> One teacher can take multiple exams

![Exams1](./picture/16.png)
