import webbrowser as wb 
import pyfiglet

word = pyfiglet.figlet_format("KAREN")
print(word)
search=input ("Search: ")

if search=="open youtube":
      wb.open('https://m.youtube.com/')
      
else:
      print ("Error")