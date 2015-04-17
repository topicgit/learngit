#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ************************************************************************
#    File Name: tab.py
#	 Author: Tempo
#	 Mail: wodetempo@163.com 
#	 Created Time: 2015年03月04日 星期三 14时47分16秒
# ************************************************************************
# python startup file

import os
import readline
import rlcompleter
import atexit
import sys

# tab completion
readline.parse_and_bind('ta: complete')
# history file
histfile = os.path.join(os.environ['HOME'],'.pythonhistory')
try:
	readline.read_history_file(histfile)
except IOError:
	pass
atexit.register(readline.write_history_file, histfile)
