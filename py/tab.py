#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ************************************************************************
#    File Name: tab1.py
#	 Author: Tempo
#	 Mail: wodetempo@163.com 
#	 Created Time: 2015年03月04日 星期三 14时51分58秒
# ************************************************************************

import sys
import readline
import rlcompleter
import os

readline.parse_and_bind('tab: complete')
histfile = os.path.join(os.environ['HOME'], '.pythonhistory')
