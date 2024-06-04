from odoo import models, fields, api

class NCCervice(models.Model):
    _name = 'ncc.service'
    _description = 'NCC Service Booking'

    id = fields.Char(string='ID', required=True, copy=False, readonly=True, index=True)
    client_email = fields.Char(string='Customer Email', required=True)
    service_datetime = fields.Datetime(string='Service Date & Time', required=True, default=fields.Datetime.now())
    departure_loc = fields.Char(string='Departure Location', required=True)
    arrival_loc = fields.Char(string='Arrival Location', required=True)

    currency_id = fields.Many2one('res.currency', string='Currency', default=126)
    price = fields.Monetary('Price')
    is_paid = fields.Boolean(string='Already Paid', required=True)

    car = fields.Many2one('fleet.vehicle', string='Car')
    driver = fields.Many2one('res.partner', string='Driver')

    @api.constrains('service_datetime')
    def _check_service_datetime(self):
        for record in self:
            if record.service_datetime < fields.Datetime.now():
                raise models.ValidationError('Service Date & Time must be in the future')
