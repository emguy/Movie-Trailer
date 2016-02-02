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
#     File Name : media.py
# Last Modified : Mon, Feb 01, 2016  3:29:14 PM

import json
import urllib

class Movie():
  """
  A Movie object which stores the meta-information about a movie.
  All movie data is retrived from the Open Movie Database (OMDB).
  
  Attributes:
    title (str):                title of the movie
    year (str):                 the year of production
    genre (str):                the genre of the movie
    plot (str):                 the plot of the movie
    director (str):             the name of the movie director
    actors (str):               
    poster_image_url (str):     the URL to the movie thumbnail
    trailer_youtube_url( str):  the URL to the movie trailer (on youtube)
  """
  # we retrive movie data from the Open Movie Database (OMDB)
  OMDB_API = "http://www.omdbapi.com/?y=&plot=short&r=json&t="

  # constructor
  def __init__(self, title, trailer_url):

    # the requesting url
    url = Movie.OMDB_API + title
    # the json response 
    response = urllib.urlopen(url, trailer_url)
    # parse json obj
    obj = json.load(response)
    
    # load the movie data
    self.title = obj["Title"]
    self.year = obj["Year"]
    self.genre = obj["Genre"]
    self.plot = obj["Plot"]
    self.director = obj["Director"]
    self.actors = obj["Actors"]
    self.poster_image_url = obj["Poster"]
    self.trailer_youtube_url = trailer_url

# This list stores an array of created movies objects
movie_list = list()

# add movie #1 
title = "Star Trek Beyond"
trailer_url = "https://www.youtube.com/watch?v=XRVD32rnzOw"
movie_list.append(Movie(title, trailer_url))

# add movie #2 
title = "10 Cloverfield Lane"
trailer_url = "https://www.youtube.com/watch?v=yQy-ANhnUpE"
movie_list.append(Movie(title, trailer_url))

# add movie #3 
title = "The Big Short"
trailer_url = "https://www.youtube.com/watch?v=dxAcIWDi8ps"
movie_list.append(Movie(title, trailer_url))

# add movie #4 
title = "Zoolander 2"
trailer_url = "https://www.youtube.com/watch?v=4CL4LNWHegk"
movie_list.append(Movie(title, trailer_url))

# add movie #5 
title = "ANOMALISA"
trailer_url = "https://www.youtube.com/watch?v=WQkHA3fHk_0"
movie_list.append(Movie(title, trailer_url))

# add movie #6 
title = "Daddy's Home"
trailer_url = "https://www.youtube.com/watch?v=Ngptwcz3-JA"
movie_list.append(Movie(title, trailer_url))

# add movie #7 
title = "The Little Prince"
trailer_url = "https://www.youtube.com/watch?v=ihi491RQo5A"
movie_list.append(Movie(title, trailer_url))

# add movie #8 
title = "13 Hours: The Secret Soldiers of Benghazi"
trailer_url = "https://www.youtube.com/watch?v=4CJBuUwd0Os"
movie_list.append(Movie(title, trailer_url))

# add movie #9 
title = "Barnyard"
trailer_url = "https://www.youtube.com/watch?v=s5soJDEbzIc"
movie_list.append(Movie(title, trailer_url))
