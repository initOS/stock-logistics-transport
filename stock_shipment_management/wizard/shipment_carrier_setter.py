# -*- coding: utf-8 -*-
#
#
#    Author: Yannick Vaucher
#    Copyright 2015 Camptocamp SA
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more description.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
#
from openerp import models, fields, api


class CarrierSetter(models.TransientModel):
    _name = "shipment.carrier.setter"
    _inherit = "shipment.value.setter"

    carrier_id = fields.Many2one(
        'delivery.carrier',
        'Carrier',
        help="Shipment carrier"
    )

    @api.multi
    def set_value(self):
        """ Changes the Shipment Carrier and update departure and arrival
        pickings """
        for setter in self:
            self.shipment_id.carrier_id = self.carrier_id
        pickings = self.shipment_id.departure_picking_ids
        pickings |= self.shipment_id.arrival_picking_ids
        to_write = pickings.filtered(
            lambda r: r.state not in ('done', 'cancel'))
        to_write.write({'carrier_id': self.carrier_id.id})
