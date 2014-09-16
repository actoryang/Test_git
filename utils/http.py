#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Collect utility about http methods.
"""

import json

JSON_CONTENT_TYPE = "application/json"


def api_response(status_code, response, data):
    """ response content-type is 'application/json'.
    """
    response.status_code = status_code
    response.set_data(json.dumps(data))
    response.headers['content-type'] = JSON_CONTENT_TYPE
