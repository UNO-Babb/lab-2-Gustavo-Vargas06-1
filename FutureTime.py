#FutureTime.py
#Name: Gustavo Vargas
#Date: 1/29/2025
#Assignment: FutureTime Lab-2

# datetime will allow us to access the system date and time.
import datetime

def main():
  #getting current time from system, storing to variable
  now = datetime.datetime.now()
  currentHour = (now.hour - 5) % 12
  currentMinute = (now.minute)

  strCHour = str(currentHour)
  strCMin = str(currentMinute)
  if currentMinute < 10:
    strCMin = "0" + strCMin
  print (strCHour + ":" + strCMin)
 #this is just for checking, we should delete it later

  #TODO:
  #Ask user for hours
  futureH = input("Enter Hours: ")

  futureH = int(futureH)

  futureHours = (currentHour + futureH) % 12
  

  #Ask user for minutes
  futureM = input("Enter minutes: ")
  futureM = int(futureM)

  #futurem = futureM % 60

  futureMinute = ((currentMinute + futureM) % 60)
  futureMin = (currentMinute + futureM) // 60
  

  #futureMinute = futureMinute + futurem

  
  


  
  strMin = str(futureMinute)
  #Calculate the time after the user-supplied time has passed.
  FutureH = futureHours + (futureMinute // 60)
  FutureH = FutureH + futureMin
  FutureH = FutureH % 12
  strHour = str(FutureH)

  if futureMinute < 10:
    strMin = "0" + strMin

  print(strHour + ":" + strMin)
  
  #Do not use any if statements in calculating the time.

  #Output the future time in standard format "HH:MM"
if __name__ == '__main__':
  main()
