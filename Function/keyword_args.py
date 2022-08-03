#we have another way in python that will
#allow us to pass name args to a func i.e called keyword args
#**kwargs
#kwargs is the name of the parameter and ** before it means that it can accept 
#any number of name values in the func 

def student_report(**kwargs):
    total = 0
    for k,v in kwagrs.items():
        print(k,v)
        total +=v
    return len(kwargs),total/len(kwargs)



 #ex call
print(student_report(rohal=30,priti=50,rani=60))
print(student_report(a=40,b=50,c=60,d=80,e=90))        