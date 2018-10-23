import pyodbc
server = 'alexasql.database.windows.net'
database = 'AdventureWorks2016'
username = 'cmps253'
password = 'Cmps205!'
driver= '{SQL Server}'

cnxn = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+password)
file2  = open("cmps209.html","w")
file = open("cmps205.html","w")

file = open("cmps205.html","w") 
 
file.write("<html>")
file.write("<head>")
file.write("<style>")
file.write("table, th, td { border: 1px solid black; }")
file.write("</style>")
file.write("</head>")

file.write("<table>")
 
hello word





test test test
