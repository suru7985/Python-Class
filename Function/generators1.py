 #wap to generate a list of acronyms from a list of word using generatros & *args
#wap to generate a list of even sqr using generators 

# def acronym(*words):
#      for word in words:
#          yield ''.join([i[0].upper() for in word.split()])

#  #ex call

# for item in acronym('Project Manager','Software Engineer', 'Data Scientist'):
#      print(item)

def acronym(*words):
    for word in words:
        yield ''.join([i[0].upper() for i in word.split()])

# ex call

for item in acronym('Project Manager','Software Engineer','Data Analyst'):
    print(item)


print(list(acronym('Project Manager','Software Engineer','Data Analyst','Team Lead',"Program tester"))) 




def even(limit):

    for i in range(1,limit+1):
        if i%2==0:
        #yield i/2
         yield i**2


for e in even (10):
    print(e)        
