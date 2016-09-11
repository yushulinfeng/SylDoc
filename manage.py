#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''默认工具文件，不必修改'''

import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "SylDoc_Server.settings")
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)
