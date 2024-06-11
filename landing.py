#!/usr/bin/python3

import cgi
import cgitb
import sys
import mysql.connector

cgitb.enable()

# database connection string
mydb = mysql.connector.connect(
  host="192.168.1.243",
  user="CHANGEME",
  password="CHANGEME",
  database="recipe_db"
)

mycursor = mydb.cursor()

sql = "SELECT \
        recipe_names.recipe_name AS recipe \
        FROM recipe_names"

mycursor.execute(sql)

myresult = mycursor.fetchall()

print('Content-type: text/html\n\n')
print('<form action="show_recipe.py">')
print('<label for="Recipe name">Recipe Name:</label> \
       <select id="name" name="name"> ')

# iterate over the SQL and generate the appropriate HTML for the list
for x in myresult:
  print('<option value="' + x[0] + '">' + x[0] + '</option>')

print('</select>')
print('<input type="submit" value="Submit">')
print('</form>')







~

