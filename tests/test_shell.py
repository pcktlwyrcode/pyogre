"""PyOgre Test Shell: a demonstration and troubleshooting shell for PyOgre
    Copyright (C) 2021  Timothy Welborn

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see https://www.gnu.org/licenses/gpl-3.0.en.html.

    See README.md for the full license text."""

__author__ = 'Timothy Welborn'
__copyright__ = 'Copyright 2021, Timothy Welborn'
__credits__ = [__author__]
__license__ = 'GPLv3'
__version__ = '0.1.0'
__maintainer__ = __author__
__email__ = 'welborntimothy@gmail.com'
__status__ = 'Prototype'

import pyogre

print("""PyOgre Test Shell  Copyright (C) 2021  Timothy Welborn

This program comes with ABSOLUTELY NO WARRANTY.
This is free software, and you are welcome to redistribute it
under certain conditions; type `license' for details.""")

ogre = pyogre.PyOgre()

command = str()

while command != 'exit':
    command = input('PyOgre test shell > ').lower().strip()

    if command == 'help':
        print("""Available commands:
        \thelp
        \tset-auth
        \tlist-markets
        \tget-order-book
        \tget-ticker
        \tget-history
        \tbuy-order
        \tsell-order
        \tcancel-order
        \tget-orders
        \tget-order
        \tget-balance
        \tget-balances
        \tlicense
        \texit""")

    elif command == 'set-auth':
        ogre.key = input('key: ')
        ogre.secret = input('secret: ')

    elif command == 'list-markets':
        print(ogre.list_markets())

    elif command == 'get-order-book':
        print(ogre.get_order_book(input('market: ')))

    elif command == 'get-ticker':
        print(ogre.get_ticker(input('market: ')))

    elif command == 'get-history':
        print(ogre.get_history(input('market: ')))

    elif command == 'buy-order':
        print(ogre.buy_order(input('market: '), input('quantity: '), input('price: ')))

    elif command == 'sell-order':
        print(ogre.sell_order(input('market: '), input('quantity: '), input('price: ')))

    elif command == 'cancel-order':
        print(ogre.cancel_order(input('uuid: ')))

    elif command == 'get-orders':
        print(ogre.get_orders(input('market: ')))

    elif command == 'get-order':
        print(ogre.get_order(input('uuid: ')))

    elif command == 'get-balance':
        print(ogre.get_balance(input('currency: ')))

    elif command == 'get-balances':
        print(ogre.get_balances())

    elif command == 'license':
        print("""PyOgre Test Shell: a demonstration and troubleshooting shell for PyOgre
Copyright (C) 2021  Timothy Welborn

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see https://www.gnu.org/licenses/gpl-3.0.en.html.

See README.md for the full license text.""")

    else:
        print('unrecognized command "{0}", type "help" for available commands'.format(command))
