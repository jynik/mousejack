#!/usr/bin/env python2
'''
  Copyright (C) 2016 Jon Szymaniak <jon.szymaniak@gmail.com>

  This program is free software: you can redistribute it and/or modify
  it under the terms of the GNU General Public License as published by
  the Free Software Foundation, either version 3 of the License, or
  (at your option) any later version.

  This program is distributed in the hope that it will be useful,
  but WITHOUT ANY WARRANTY; without even the implied warranty of
  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
  GNU General Public License for more details.

  You should have received a copy of the GNU General Public License
  along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''

from __future__ import print_function
import sys
from lib import common

# Parse command line arguments and initialize the radio
common.init_args('./nrf24-dump-flash.py')
common.parser.add_argument('-o', '--output', type=str, help='Output file', required=True)
common.parser.add_argument('-m', '--memory', type=int, help='# kbytes of on-chip memory. (16 or 32)', default=32)
common.parse_and_init()

addr = 0
read_len = 16
addr_max = common.args.memory * 1024

outfile = open(common.args.output, 'wb')

while addr < addr_max:
    read_data = common.radio.spi_flash_read(addr, read_len)
    outfile.write(read_data)
    addr += read_len
