# -*- coding: utf-8 -*-
#
# Copyright (C) Pootle contributors.
#
# This file is a part of the Pootle project. It is distributed under the GPL3
# or later license. See the LICENSE file for a copy of the license and the
# AUTHORS file for copyright and authorship information.

import importlib

from django.apps import AppConfig


class PootleDataConfig(AppConfig):

    name = "pootle_data"
    verbose_name = "Pootle Data"
    version = "0.0.6"

    def ready(self):
        importlib.import_module("pootle_data.models")
        importlib.import_module("pootle_data.getters")
        importlib.import_module("pootle_data.receivers")
