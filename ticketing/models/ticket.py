from odoo import models, fields, api
from odoo.exceptions import ValidationError


class Ticket(models.Model):
    _name = 'ticketing.ticket'
    _description = 'Ticket'

    description = fields.Char('Description')
    reservation_id = fields.Many2one('ticketing.reservation', string='Reservation', required=True)
    client_id = fields.Many2one('ticketing.client', string='Client', related='reservation_id.client_id', store=True)
    employee_id = fields.Many2one('hr.employee', string='Employee', required=True)
    type = fields.Selection([
        ('claim', 'Reclamation'),
        ('query', 'Query'),
        ('suggestion', 'Suggestion')
    ], string='Type', required=True)
    state = fields.Selection([
        ('created', 'Created'),
        ('pending', 'Pending Confirmation'),
        ('denied', 'Denied'),
        ('processed', 'Processed Successfully')
    ], string='State', default='created')
