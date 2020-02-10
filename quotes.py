from bs4 import BeautifulSoup
import pyfiglet,colorama,termcolor,random
from requests import get
from csv import writer
from os import system, name 
import random

def clear(): 
  

    if name == 'nt': 
        _ = system('cls') 

    else: 
        _ = system('clear') 

count = 1
request=True
quotes_text= []
while count<11:
    try:
        request = get(f"http://quotes.toscrape.com/page/{count}/")
        count = count+1
        quotes = BeautifulSoup(request.text,"html.parser")
        clear()
        quotes_tags = quotes.find_all(class_="quote")

        for quote in quotes_tags:
            quotes_text.append([quote.find(class_="text").get_text(),
            quote.find(class_="author").get_text(),
            quote.find("a")["href"]
            ])   

    except:
        break


quote_choose = random.randint(0,len(quotes_text))


# Action Time
colorama.init()
print(termcolor.colored(pyfiglet.figlet_format("Italo Quotes"),color="red"))

guesses= 4
while True:
    if(guesses==4):
       print("Here's a quote:")
       print(quotes_text[quote_choose][0])
    elif(guesses==3):

        about = BeautifulSoup(get(f"http://quotes.toscrape.com/{quotes_text[quote_choose][2]}").text,"html.parser")
        about = about.find(class_="author-description").get_text()
        position_name = about.find(quotes_text[quote_choose][1])
        position_A = about.find(".",position_name+len(quotes_text[quote_choose][1])+1,len(about))
        position_B = about.find(".",position_A+1,len(about))
        about_author = about[position_A+1:position_B+1]
      
        print(termcolor.colored("Here's a hint : ",color="yellow"))
        print(about_author)
    elif(guesses==2):
        print(termcolor.colored("Here's a hint : ",color="yellow"))
        print(f"the author's first name start with:{quotes_text[quote_choose][1][0]}")
    elif(guesses==1):
        print(termcolor.colored("Here's a hint : ",color="yellow"))
        print(f"the author's name ends with:{quotes_text[quote_choose][1][len(quotes_text[quote_choose][1])-1]}")
    else:
        print(f"You lose the answer was {quotes_text[quote_choose][1]}")
        play = input("Would you like to play again? Y/N  ")
        if  play[0] == "y" or play[0]=="Y":
            clear()
            quote_choose = random.randint(0,len(quotes_text))
            guesses= 4
            continue
        else:
            break
    answer = input(f"\n Who said this? Guesses Remaining: {guesses}. ")
    if (answer == quotes_text[quote_choose][1]):
        print("You guessed correctly,Congratulations!!!")
        play = input("Would you like to play again? Y/N")
        if  play[0] == "y" or play[0]=="Y":
            clear()
            quote_choose = random.randint(0,len(quotes_text))
            guesses= 4
            continue
        else:
            break
    else:
        guesses -= 1
    print("\n")

    



