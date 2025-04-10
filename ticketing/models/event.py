from odoo import models, fields, api


class Event(models.Model):
    _name = 'ticketing.event'
    _description = 'Event'

    name = fields.Char(string='Event Name', required=True)
    description = fields.Text(string='Description', required=True)
    date = fields.Datetime(string='Date', required=True)
    time = fields.Float(string='Duration (minutes)', required=True)
    available_tickets = fields.Integer(string="Total event tickets", required=True)
    location = fields.Char(string='Location', required=True)
    price = fields.Float(string='Price', required=True)
    reservation_ids = fields.One2many('ticketing.reservation', 'event_id', string='Reservations')

    # Computed field to get the number of tickets taken (via reservations)
    taken_tickets = fields.Integer(
        string='Taken Tickets',
        compute='_compute_taken_tickets',
        store=True
    )

    @api.depends('reservation_ids')
    def _compute_taken_tickets(self):
        for event in self:
            event.taken_tickets = len(event.reservation_ids)