#the survey questions

i = 0
input "How would you describe yourself?     (i)Introvert    (a)Ambivert     (e)Extrovert"

#the grouping

if i=i:
    introvert()
elif i=a:
    ambivert()
elif i=e:
    extrovert()
else:
    #prompt to answer correctly