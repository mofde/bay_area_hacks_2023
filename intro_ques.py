#the survey questions

#define classes
class introvert(object):
    #constructor
    def _init_(self):
        self._description = findDescription(input("How would you describe yourself? (c)Creative (s)Smart (e)Easygoing (i)Insightful"))
        self._hobby = findHobby(input("What do you prefer to do in your spare time? (v)Video games (c)Creative activities (s)Sports (t)Technology"))
        self._landscape = findLandscape(input("What kind of landscape do you prefer? (f)Forest (c)City (o)Ocean (m)Mountains"))
        self._movie = findMovie(input("What kinds of movie do you prefer? (a)Action (r)Romance (c)Comedy (d)Drama"))

class ambivert(object):
    #constructor
    def _init_(self):
        self._description = findDescription(input("How would you describe yourself? (c)Creative (s)Smart (e)Easygoing (i)Insightful"))
        self._hobby = findHobby(input("What do you prefer to do in your spare time? (v)Video games (c)Creative activities (s)Sports (t)Technology"))
        self._landscape = findLandscape(input("What kind of landscape do you prefer? (f)Forest (c)City (o)Ocean (m)Mountains"))
        self._movie = findMovie(input("What kinds of movie do you prefer? (a)Action (r)Romance (c)Comedy (d)Drama"))
    
class extrovert(object):
    #constructor
    def _init_(self):
        self._description = findDescription(input("How would you describe yourself? (c)Creative (s)Smart (e)Easygoing (i)Insightful"))
        self._hobby = findHobby(input("What do you prefer to do in your spare time? (v)Video games (c)Creative activities (s)Sports (t)Technology"))
        self._landscape = findLandscape(input("What kind of landscape do you prefer? (f)Forest (c)City (o)Ocean (m)Mountains"))
        self._movie = findMovie(input("What kinds of movie do you prefer? (a)Action (r)Romance (c)Comedy (d)Drama"))

#identify personality type
def ask():
    i = input("How would you describe yourself?     (i)Introvert    (a)Ambivert     (e)Extrovert")

    #the grouping
    #sort people into classes
    if i=="i":
        newPerson = introvert()
    elif i=="a":
        newPerson = ambivert()
    elif i=="e":
        newPerson = extrovert()
    else:
        #prompt to answer correctly
        prompt()

#correct for user error
def prompt():
    i = input("Invalid input! How would you describe yourself?     (i)Introvert    (a)Ambivert     (e)Extrovert")
    if i=="i":
        newPerson = introvert()
    elif i=="a":
        newPerson = ambivert()
    elif i=="e":
         newPerson = extrovert()

#sort answers to questions
def findDescription(description):
    description = description.lower()
    if description == "c":
        return "creative"
    elif description == "s":
        return "smart"
    elif description == "e":
        return "easygoing"
    elif description == "i":
        return "insightful"

def findHobby(hobby):
    hobby = hobby.lower()
    if hobby == "v":
        return "video games"
    elif hobby == "c":
        return "creative activities"
    elif hobby == "s":
        return "sports"
    elif hobby == "t":
        return "technology"

def findLandscape(landscape):
    landscape = landscape.lower()
    if landscape == "f":
        return "forest"
    if landscape == "o":
        return "ocean"
    if landscape == "c":
        return "city"
    if landscape == "m":
        return "mountains"

def findMovie(movie):
    movie = movie.lower()
    if movie == "a":
        return "action"
    elif movie == "r":
        return "romance"
    elif movie == "c":
        return "comedy"
    elif movie == "d":
        return "drama"

def groups():
    