#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

FILENAME = 'en_QS.dic'
with open(FILENAME, 'r+') as f:
    lines = f.read().splitlines()
    firstline = lines[0]
    lines = lines[1:]
    lines.sort()
    lines.insert(0, firstline)
    f.seek(0)
    f.write('\n'.join(lines))
