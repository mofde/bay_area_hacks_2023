#the survey questions

#variable

#ask input
def ask():
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
        prompt()

def prompt():
    i = input("Invalid input! How would you describe yourself?     (i)Introvert    (a)Ambivert     (e)Extrovert")
    if i=="i":
        introvert()
    elif i=="a":
        ambivert()
    elif i=="e":
        extrovert()