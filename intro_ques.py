#the survey questions

#variable
i = 0

#ask input
input "How would you describe yourself?     (i)Introvert    (a)Ambivert     (e)Extrovert"

#the grouping
#make all categories as functions to be used later, these need to store the data of people
if i=i:
    introvert()
elif i=a:
    ambivert()
elif i=e:
    extrovert()
else:
    #prompt to answer correctly