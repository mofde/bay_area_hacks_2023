#the survey questions

#variable

#ask input

class Person(object):
    #constructor
    def _init_(self):
        self._sociality = input("How would you describe yourself?     (i)Introvert    (a)Ambivert     (e)Extrovert")
        self._description = input("How would you describe yourself? (c)Creative (s)Smart (e)Easygoing (i)Insightful")
        self._hobby = input("What do you prefer to do in your spare time? (v)Video games (c)Creative activities (s)Sports (t)Technology")
        self._landscape = input("What kind of landscape do you prefer? (f)Forest (c)City (o)Ocean (m)Mountains")
        self._movie = input("What kinds of movie do you prefer? (a)Action (r)Romance (c)Comedy (d)Drama")

"""def ask():
    i = input("How would you describe yourself?     (i)Introvert    (a)Ambivert     (e)Extrovert")

    #the grouping
    #make all categories as functions to be used later, these need to store the data of people
    if i=="i":
        introvert()
    elif i=="a":
        ambivert()
    elif i=="e":
        extrovert()
    else:
        #prompt to answer correctly
        prompt()"""

"""def prompt():
    i = input("Invalid input! How would you describe yourself?     (i)Introvert    (a)Ambivert     (e)Extrovert")
    if i=="i":
        introvert()
    elif i=="a":
        ambivert()
    elif i=="e":
        extrovert()"""