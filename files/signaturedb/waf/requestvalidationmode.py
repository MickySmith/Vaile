#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# -:-:-:-:-:-:-:-:-:-:-:-:#
#    Vaile Framework     #
# -:-:-:-:-:-:-:-:-:-:-:-:#

# Author: @_tID (Modified version from wascan)
# This module requires Vaile Framework
# https://github.com/VainlyStrain/Vaile

from re import search


def requestvalidationmode(headers, content):
    detect = False
    detect |= search(r'ASP.NET has detected data in the request that is potentially dangerous', content) is not None
    detect |= search(r'Request Validation has detected a potentially dangerous client input value', content) is not None
    if detect:
        return "ASP.NET RequestValidationMode (Microsoft)"
