#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2019 zach <zach@zach-blade>
#
# Distributed under terms of the MIT license.

"""
Concatenates all class notes into a single pdf
"""

import sys, os
from pathlib import Path

fs = [str(fn) for fn in Path('.').glob('day*/*.pdf')]
fs = sorted(fs, key=lambda x: int(x.split('/')[0][3:]))
of = "MLSP_Notes.pdf"
args = fs
args.insert(0, 'pdfunite')
args.append(of)

os.popen(" ".join(args))
