#!/usr/bin/env python
# -*- coding: utf-8 -*-

from jinja2 import Environment, FileSystemLoader
import os


class JinjaConfig:
    BASE_DIR = os.path.abspath(os.curdir)
    _loader = FileSystemLoader(os.path.join(BASE_DIR, 'templates'))
    JINJA_ENVIRONMENT = Environment(loader=_loader)
