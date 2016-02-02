# -*- coding: utf-8 -*-
##############################################################################
#
#    Author: Rami Alwafaie
#    Copyright 2015 initOS GmbH
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{'name': 'Migration Multiple Carrier',
 'version': '1.0',
 'category': '',
 'description': """
Migration - Multiple Carrier
=======================================

* Install this module to trigger the old carrier id and carrier references.
""",
 'depends': ['stock_picking_multiple_carrier',
             ],
 'author': "initOS GmbH",
 'license': 'AGPL-3',
 'data': ['trigger.xml',
 ],
 'installable': True,
 'application': False,
 }