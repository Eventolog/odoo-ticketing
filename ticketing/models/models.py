from odoo import models, fields, api
from datetime import date

class Ticketing(models.Model):
    _name = 'ticketing.ticketing'
    _description = 'Ticketing'

class TicketingStudent(models.Model):
    _name = 'ticketing.student'
    _description = 'ticketing students'

    name = fields.Char('Name', required=True)
    last_name = fields.Char(string="Last Name", required=True)
    birthdate = fields.Date('Birthdate')
    id_number = fields.Char('ID', size=64, required=True)
    active = fields.Boolean('Active', default=True, help="Is the student currently part of the class?")
    age = fields.Integer('Age', compute='_age_compute')
    class_id = fields.Many2one('ticketing.ticketing_class', string="Class")
    event_ids = fields.Many2many('ticketing.event', string="Events")

    _sql_constraints = [('id_number_uniq', 'unique (id_number)', "Student ID already exists!")]

    @api.depends('birthdate')
    def _age_compute(self):
        for record in self:
            if record.birthdate:
                today = date.today()
                age = today.year - record.birthdate.year
                if today.month < record.birthdate.month or (today.month == record.birthdate.month and today.day < record.birthdate.day):
                    age -= 1
                record.age = age
            else:
                record.age = 0

class TicketingClass(models.Model):
    _name = 'ticketing.ticketing_class'

    _description = 'ticketing Classes'

    name = fields.Char('Denomination', size=64, required=True)
    grade = fields.Selection([
        ('first', 'First grade'),
        ('second', 'Second grade'),
        ('third', 'Third grade'),
        ('fourth', 'Fourth grade'),
    ], default='first')
    date_begin = fields.Date('Date begin')
    date_end = fields.Date('Date end')
    tutor_id = fields.Many2one('hr.employee', string='Tutor')
    student_ids = fields.One2many('ticketing.student', 'class_id', string='ticketing')
    student_number = fields.Integer('Student number', compute='_compute_student_number', store=True)
    description = fields.Text('Description')

    @api.depends('student_ids')
    def _compute_student_number(self):
        for record in self:
            record.student_number = len(record.student_ids)

    @api.model
    def create(self, vals):
        """Override create to ensure `student_number` is correctly calculated"""
        new_class = super(TicketingClass, self).create(vals)
        # Recompute student number when a class is created
        new_class._compute_student_number()
        return new_class

class Event(models.Model):
    _name = 'ticketing.event'
    _order = 'datetime_begin'

    name = fields.Char('Denomination', size=64, required=True)
    type = fields.Selection([
        ('absence', 'Absence'),
        ('delay', 'Delay'),
        ('felicitation', 'Felicitation'),
        ('behavior', 'Behavior')
    ], default='felicitation')
    class_id = fields.Many2one('ticketing.ticketing_class', 'Class')
    datetime_begin = fields.Datetime('Datetime', default=fields.Datetime.now())
    student_ids = fields.Many2many('ticketing.student', string='Students')
    description = fields.Text('Description')
    teacher_id = fields.Many2one('hr.employee', string="Teacher")

    @api.model
    def create(self, vals):
        if 'class_id' in vals and vals['class_id']:
            ticketing_class = self.env['ticketing.ticketing_class'].browse(vals['class_id'])
            class_name = ticketing_class.name
            event_type = dict(self._fields['type'].selection).get(
                vals.get('type', 'felicitation'))
            vals['name'] = f"({class_name}) {event_type}"
        else:
            event_type = dict(self._fields['type'].selection).get(vals.get('type', 'felicitation'))
            vals['name'] = f"{event_type}"

        return super(Event, self).create(vals)

    def write(self, vals):
        if 'class_id' in vals or 'type' in vals:
            class_name = self.class_id.name if 'class_id' not in vals else self.env['ticketing.ticketing_class'].browse(
                vals['class_id']).name
            event_type = dict(self._fields['type'].selection).get(vals.get('type', self.type))
            vals['name'] = f"({class_name}) {event_type}"

        return super(Event, self).write(vals)

