from odoo import models, fields, api

class Client(models.Model):
    _name = 'ticketing.client'
    _description = 'Client'

    name = fields.Char(string='First Name', required=True)
    surname = fields.Char(string='Last Name', required=True)
    phone = fields.Char(string='Phone', required=True)
    address = fields.Text(string='Address')
    email = fields.Char(string='Email', required=True)
    reservation_ids = fields.One2many('ticketing.reservation', 'client_id', string='Reservations')
    ticket_ids = fields.One2many('ticketing.ticket', 'client_id', string='Tickets')