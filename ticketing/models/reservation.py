from odoo import models, fields, api
from odoo.exceptions import ValidationError


class Reservation(models.Model):
    _name = 'ticketing.reservation'
    _description = 'Reservation'

    client_id = fields.Many2one('ticketing.client', string='Client', required=True)
    event_id = fields.Many2one('ticketing.event', string='Event', required=True)
    ticket_ids = fields.One2many('ticketing.ticket', 'reservation_id', string='Tickets')
    name = fields.Char('Reservation Name', compute='_compute_name', store=True)

    @api.depends('event_id', 'client_id')
    def _compute_name(self):
        for record in self:
            if record.event_id and record.client_id:
                event_name = record.event_id.name if record.event_id else ''
                client_name = record.client_id.name if record.client_id else ''
                record.name = f"{event_name} / {client_name}"

    @api.model
    def _str_(self):
        # Return the computed name in string representation
        return self.name

    @api.constrains('event_id')
    def _check_max_tickets(self):
        for reservation in self:
            event = reservation.event_id
            if event:
                # Count the tickets for the event (excluding the current reservation's tickets)
                ticket_count = self.env['ticketing.reservation'].search_count([
                    ('event_id', '=', event.id)
                ])

                # Validate if the number of tickets does not exceed the available tickets
                if ticket_count > event.available_tickets:
                    raise ValidationError(
                        f"The number of tickets for this event has reached the maximum limit of {event.available_tickets}."
                    )

