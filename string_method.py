# str = "this is the python 3.0 and this programer execute this code";
# print("str.capitalize() :",str.capitalize());
# sub ="t"
# print(f"this is center method : ",str.count(sub,1,50));
# sub ="this";
# print("this is count method :",str.count(sub))
# str = "this is string example ..... wow!!!";
# str = str.encode('base64','strict')
# print("this is encode " +str)
# print("this decode string :" +str.decode('base64','strict'))
# str ="this is \tstring example....wow!!!";
# suffix ="wow!!!";
# print(str.endswith(suffix));
# print(str.endswith(suffix,20));
# suffix ="is";
# print(str.endswith(suffix,2,4));
# print(str.endswith(suffix,2,6));
# print("Original string :"+str);
# print("Default exapanded tab:" +str.expandtabs());
# print("double exapanded tab:" +str.expandtabs(0))
# str1 = "this is string example...wow!!!";
# str2 ="exam";
# print(str1.index(str2))
# print(str1.index(str2,10)))
# Get data from fields
# print(str1.index(str2,30))
# str = "this"; # No space & digit in this string
# print (str.isalpha());
# str = ("this is string example....wow!!!");
# print (str.isalpha());
# import time;
# localtime = time.asctime(time.localtime(time.time()))
# print ("Local current time :", localtime)
# import calendar
# cal = calendar.month(2020, 1)
# print ("Here is the calendar:", calendar.month(2020, 1))
# print (cal);
# def KelvinToFahrenheit(Temperature):
#     assert ((Temperature >= 0),"Colder than absolute zero!")
#     return (((Temperature-273)*1.8)+32)
# print (KelvinToFahrenheit(273))
# print (int(KelvinToFahrenheit(505.78)))
# print (KelvinToFahrenheit(-5))
# class Employee:
#     'Common base class for all employees'
#     empCount = 0
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary
#         Employee.empCount += 1
#     def displayCount(self):
#         print ("Total Employee %d" %d Employee.empCount)
#     def displayEmployee(self):
#         (print "Name : ", self.name, ", Salary: ", self.salary)
# import cgi, cgitb
# Create instance of FieldStorage
# form = cgi.FieldStorage(
# first_name = form.getvalue('first_name')
# last_name = form.getvalue('last_name')
# print ("Content-type:text/html\r\n\r\n")
# print ("<html>")
# print ("<head>")
# print ("<title>Hello - Second CGI Program</title>")
# print ("</head>")
# print ("<body>")
# print ("<h2>Hello %s %s</h2>" % (first_name, last_name))
# print ("</body>")
# print ("</html>")
# import smtplib
# message = """From: From Person <from@fromdomain.com>
# To: To Person <to@todomain.com>
# MIME-Version: 1.0
# Content-type: text/htmlyygh
# Subject: SMTP HTML e-mail test
# This is an e-mail message to be sent in HTML format
# <b>This is HTML message.</b>
# <h1>This is headline.</h1>
# """
# try:
#     smtpObj = smtplib.SMTP('localhost')
#     smtpObj.sendmail(sender, receivers, message)
#     print ("Successfully sent email")
# except SMTPException:
#     print ("Error: unable to send email")
import Tkinter
import tkMessageBox
top = Tkinter.Tk()
def helloCallBack():
    tkMessageBox.showinfo( "Hello Python", "Hello World")
B = Tkinter.Button(top, text ="Hello", command = helloCallBack)
B.pack()
top.mainloop()