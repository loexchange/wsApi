#!/usr/bin/env python3
from setuptools import setup

setup(
    name="loex-client",
    version="2.0.0",
    packages=['loex',
              'loex.exception', 
              'loex.constant',
              'loex.utils',
              'loex.client',
              'loex.service', 
              'loex.service.account', 
              'loex.service.market',
              'loex.service.trade',
              'loex.model', 
              'loex.model.account', 
              'loex.model.market', 
              'loex.model.trade',
              'loex.connection', 
              'loex.connection.impl', 
              "performance", 
              "tests"
              ],
    install_requires=['requests', 'apscheduler', 'websocket-client', 'urllib3']
)
