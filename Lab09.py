import re

#Q3
def isEmail(inp):
    result=re.search(r'\w+@\w+(\.\w{2,4})', inp) 
    if result==None:
        return False
    else:return True
print isEmail('blah@hello.com')
print
print isEmail('sd$sd@hello.com')
print





#Q4
def getTxts(files):
    return re.search(r'\s\w\.\txt$\s', files)
    
print getTxts('yo.html blah.txt woah.txt he')

#Q5
def percAwesome(inp):
    result=re.search(r'(awesome|awes0me)',inp)
    if result==None:
            return False
    return result.group(1)

print percAwesome('iamawesomeblah and awes0me is as awesomeo does')
