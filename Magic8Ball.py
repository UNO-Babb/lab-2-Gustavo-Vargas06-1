#Magic8Ball.py
#Name: Gustavo Vargas
#Date: 1/29/2025
#Assignment: 8 Ball Lab-2

#We will need random for this program, import to use this package.
import random

def main():
  #Create a list of your responses.
  print("Magic 8 Ball")
  answer = ("As I see it, yes", "Ask again later", "Better not tell you now.", "Cannot predict now.",
           "Concentrate and ask again.", "Don't count on it.", "It is certain.", "It is decidedly so.", 
           "Most likely.", "My reply is no.", "My sources say no.", "Outlook not so good.", "Outlook good.", 
           "Reply hazy, try again.", "Signs point to yes.", "Very doubtful.", "Without a doubt.", 
           "Yes.", "Yes - definitely.", "You may rely on it.")
  #Prompt the user for their question.

  #Answer question randomly with one of the options from your earlier list.
  num = random.random()
  num = num * 1000
  num = int(num)
  num = num % 20 
  question = input("Ask me a question:")
  print(answer[num])
if __name__ == '__main__':
  main()
