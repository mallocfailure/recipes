#!/usr/bin/python3

import cgi
import cgitb
import sys
import mysql.connector

cgitb.enable(logdir="/logs")

mydb = mysql.connector.connect(
  host="192.168.1.243",
  user="CHANGEME",
  password="CHANGEME",
  database="recipe_db"
)

# get the parameters passed in by the HTML POST
form = cgi.FieldStorage()
recipename = form['name'].value

print('Content-type: text/html\n\n')
mycursor = mydb.cursor()
print('<h1>' + recipename + '</h1>')

# build the ingredient table

sql = "SELECT \
        recipe_names.recipe_name AS recipe, \
        ingredients.ingredient_name as ingredient, \
        ingredients.ingredient_uom as ingredient_uom, \
        ingredients.ingredient_amount as ingredient_amount \
        FROM recipe_names \
        JOIN ingredients ON recipe_names.name_pk = ingredients.recipe_fk \
        WHERE recipe_names.recipe_name = '%s'" % recipename

mycursor.execute(sql)
myresult = mycursor.fetchall()

print('<table>' \
        '<tr>' \
        '<th>Amount</th>' \
        '<th>UOM</th>' \
        '<th>Ingredient</th>' \
        '</tr>')


for x in myresult:
    print('<td>' + str(x[3]) + '</td>' \
            '<td>' + str(x[2]) + '</td>' \
            '<td>' + str(x[1]) + '</td>' \
            '</tr>')

print('</table>')

# build the instructions section
sql = "SELECT \
        recipe_names.recipe_name as recipe, \
        instructions.instruction_text as instruction_text \
        from recipe_names \
        join instructions ON recipe_names.name_pk = instructions.recipe_fk \
        WHERE recipe_names.recipe_name = '%s'" % recipename

mycursor.execute(sql)
myresult = mycursor.fetchall()

for x in myresult:
    fixed = str(x[1])
    fixed = fixed[2:]
    fixed = fixed.replace('\\n', '<br>')
    print('<br>' + fixed)



