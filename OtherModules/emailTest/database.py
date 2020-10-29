import mysql.connector
from decimal import Decimal
mydb = mysql.connector.connect(
  host="localhost",
  user="admin",
  passwd="admin1234",
  database="test"

)


mycursor = mydb.cursor()


# mycursor.execute("SHOW TABLES")



# for x in mycursor:

#     print (x)


# mycursor.execute("Select stddev(T_SHT2X),avg(T_SHT2X) From TwoMeterNode")
# sd = mycursor.fetchall()
# print(sd[0][0])
# print(sd[0][1])


mycursor.execute("Select T_SHT2X From TwoMeterNode")

arr= []
for x in mycursor.fetchmany(10):
  print(x[0])
  arr.append(float(x[0]))

print(arr)


# SD=Decimal(sd[0][0])

# AVG=Decimal(sd[0][1])

#mycursor.execute("Select T_SHT2X From TwoMeterNode")

#mycursor.execute ("SELECT CAST(COALESCE(T_SHT2X, 0) AS DECIMAL(10,3)) FROM TwoMeterNode")

# for x in mycursor.fetchall():
#     print(float(x[0]))
#     grub=round((float(x[0])-AVG)/SD, 3)

#     print(grub)
#grub = [(x[0]-AVG)/SD for x in mycursor.fetchall()]




