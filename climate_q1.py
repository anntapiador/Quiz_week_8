import sqlite3
import matplotlib.pyplot as plt

connection = sqlite3.connect(r"C:\Users\ajtor\OneDrive - Griffith University\04. Software Technologies\Quiz\Quiz_week_8\climate.db")
cursor = connection.cursor()
cursor.execute("SELECT* FROM ClimateData")
result = cursor.fetchall()

years = [row[0] for row in result]
co2 = [row[1] for row in result]
temp = [row[2] for row in result]

plt.subplot(2, 1, 1)
plt.plot(years, co2, 'b--') 
plt.title("Climate Data") 
plt.ylabel("[CO2]") 
plt.xlabel("Year (decade)") 

plt.subplot(2, 1, 2)
plt.plot(years, temp, 'r*-') 
plt.ylabel("Temp (C)") 
plt.xlabel("Year (decade)") 
plt.show() 
plt.savefig("co2_temp_1.png") 

connection.close()