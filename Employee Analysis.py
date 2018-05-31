import pandas as pd
import matplotlib.pyplot as p
details=pd.read_csv('u.user',sep='|',names=["User_Id","Age","Gender","Occupation","Zip_code"])
age=details.Age
gender=details.Gender
occupation=details.Occupation

malegender=gender[gender=='M'].count()
femalegender=gender[gender=='F'].count()


technician=occupation[occupation=='technician'].count()
writer=occupation[occupation=='writer'].count()
executive=occupation[occupation=='executive'].count()
admin=occupation[occupation=='administrator'].count()
stud=occupation[occupation=='student'].count()
law=occupation[occupation=='lawyer'].count()
edu=occupation[occupation=='educator'].count()
scientist=occupation[occupation=='scientist'].count()
enter=occupation[occupation=='entertainment '].count()
prog=occupation[occupation=='programmer'].count()
lib=occupation[occupation=='librarian'].count()
engi=occupation[occupation=='engineer'].count()
art=occupation[occupation=='artist'].count()
mark=occupation[occupation=='marketing'].count()
home=occupation[occupation=='homemaker'].count()
other=occupation[occupation=='other'].count()
retired=occupation[occupation=='retired'].count()
health=occupation[occupation=='healthcare'].count()
doc=occupation[occupation=='doctor'].count()
none=occupation[occupation=='none'].count()
sales=occupation[occupation=='salesman'].count()

age20=age[age<=20].count()
age40=age[(age>20)&(age<=40)].count()
age60=age[(age>40)&(age<=60)].count()
agegt60=age[age>60].count()

fig=p.figure()
fig.set_size_inches(20,10)

graph1=fig.add_subplot(2,2,1)
graph2=fig.add_subplot(2,2,2)
graph3=fig.add_subplot(2,1,2)

val=[malegender,femalegender]
val1=[age20,age40,age60,agegt60]
val2=[executive,admin,writer,technician,
      engi,doc,lib,none,prog,
      sales,other,enter,stud,health,edu,law,
      retired,home,mark,art]



graph1.axis('equal')
graph2.axis('equal')
graph3.axis('equal')

graph1.set_title("GENDER")
graph2.set_title("AGE")
graph3.set_title("OCCUPATION")

label1=["MALE","FEMALE"]
label2=["<=20",">20 AND <=40",">40 AND <=60",">60"]
label3=["EXECUTIVE","ADMIN","WRITER","TECHNICIAN",
        "ENGINEER","DOCTOR","LIBRARIAN","NONE","PROGRAMMER",
        "SALESMAN","OTHER","ENTERTAINMENT","STUDENT","HEALTH","EDUCATOR","LAWYER",
        "RETIRED","HOMEMAKER","MARKETING","ARTIST"]


graph1.pie(val,labels=label1)
graph2.pie(val1,labels=label2)
graph3.pie(val2,labels=label3)

graph1.legend(title="Gender",loc="center left")
graph2.legend(title="Age",loc="center left")
graph3.legend(title="Occupation",loc="best")



p.subplots_adjust(left=0.00,right=1.00,top=0.96,bottom=0.02)
p.savefig('Employee Analysis.png')
