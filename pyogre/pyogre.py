"""PyOgre: Python bindings for the TradeOgre API v1
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
__version__ = '1.0.0'
__maintainer__ = __author__
__email__ = 'welborntimothy@gmail.com'
__status__ = 'Production'

import requests
from requests.auth import HTTPBasicAuth
import json


class PyOgre(object):
    """TradeOgre API v1 bindings. See https://tradeogre.com/help/api for more information."""
    def __init__(self, key: str = None, secret: str = None):
        self.endpoint = 'https://tradeogre.com/api/v1/'
        self.key, self.secret = key, secret

    """Public API calls"""

    """Send a public API request over HTTP"""
    # returned type may be either dict or list
    def send_public(self, api_call: str):
        return json.loads(requests.get(self.endpoint + api_call).text)

    """Get a list of all markets with price, volume, high, low, bid, and ask"""
    def list_markets(self) -> list:
        return self.send_public('markets')

    """Get the current order book for given market"""
    def get_order_book(self, market: str) -> dict:
        return self.send_public('orders/{0}'.format(market))

    """Get the ticker for the given market in the last 24 hours"""
    def get_ticker(self, market: str) -> dict:
        return self.send_public('ticker/{0}'.format(market))

    """Get the history of the last 100 recent trades for the given market using UNIX UTC timestamp"""
    def get_history(self, market: str) -> list:
        return self.send_public('history/{0}'.format(market))

    """Private API calls"""

    """Send a private API request over HTTP using API keys"""
    # returned type may be either dict or list
    def send_private(self, api_call: str, params: dict = None, post: bool = True):
        # mutability fix
        if params is None:
            params = {}
        if self.key is None:
            raise TypeError('PyOgre.key must be type \'str\', got \'{0}\''.format(type(self.key)))
        if self.secret is None:
            raise TypeError('PyOgre.secret must be type \'str\', got \'{0}\''.format(type(self.secret)))
        if not post:
            return json.loads(requests.get(
                self.endpoint + api_call, params, auth=HTTPBasicAuth(self.key, self.secret)
            ).text)
        else:
            return json.loads(requests.post(
                self.endpoint + api_call, params, auth=HTTPBasicAuth(self.key, self.secret)
            ).text)

    """Submit a buy order to the book for the given market"""
    def buy_order(self, market: str, quantity: str, price: str) -> dict:
        return self.send_private('order/buy', {'market': market, 'quantity': quantity, 'price': price})

    """Submit a sell order to the book for the given market"""
    def sell_order(self, market: str, quantity: str, price: str) -> dict:
        return self.send_private('order/sell', {'market': market, 'quantity': quantity, 'price': price})

    """Cancel an order on the order book by UUID"""
    def cancel_order(self, uuid: str) -> dict:
        return self.send_private('order/cancel', {'uuid': uuid})

    """Get the active orders on your account"""
    def get_orders(self, market: str) -> list:
        return self.send_private('account/orders', {'market': market})

    """Get information about an order by UUID"""
    def get_order(self, uuid: str) -> dict:
        # uses GET instead of POST
        return self.send_private('account/order/{0}'.format(uuid), post=False)

    """Get the balance of a given currency on your account"""
    def get_balance(self, currency: str) -> dict:
        return self.send_private('account/balance', {'currency': currency})

    """Get all the balances on your account"""
    def get_balances(self) -> dict:
        # uses GET instead of POST
        return self.send_private('account/balances', post=False)
