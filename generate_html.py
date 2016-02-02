#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# NOTE: This program is free software; you can redistribute it 
# and/or modify it under the terms of the GNU General Public 
# License as published by the Free Software Foundation; either 
# version 3, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# Bugs can be reported to Yu Zhang <emguy2000@gmail.com>.
#
#     File Name : generate_html.py
# Last Modified : Mon, Feb 01, 2016  3:34:10 PM

from media import movie_list
import fried_tomatoes

# generate the target html file
fried_tomatoes.open_movies_page(movie_list)

