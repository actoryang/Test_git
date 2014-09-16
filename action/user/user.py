#!/usr/bin/env python
# -*- coding: utf-8 -*-

from engine import url
from utils import http


@url("/login")
def login(request, response):
    data = {"code": 200, "msg": "hello world!"}
    http.api_response(200, response, data)
