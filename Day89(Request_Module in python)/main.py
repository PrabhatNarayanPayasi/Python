# import requests
# req = requests.get("https://www.google.com");
# print(req.text);

'''
is module ka use hota haii  http request maene ke liye 

'''
'''
Python me request module ek popular module hai jiska use https 
request ko handel karne ke liye kiya jata hai 
ye http req bhejne aur response se dat fetch 
karne ke liye use hoti hai . ye http method
GET , POST , PUT DELETE method ko handle karne me 
use hota hai


'''

# import requests
# url = requests.get("http://google.com");
# print(url.text)  # ye website ka html data aur json data ko print karta hai






'''

========================WEB SCRAPING==============================================


bs4 (beautifulSoup) module hai iska use web scraping ke liye kiya jata hai
ye python ki ek library hai . 
ye html , xml document. ko parse karn ke liye . 
web pages se data ko extract karne ke liye use hoti hai 
kisi code ko html structure ke through navigate karne ke liye 
kiya jata hai . 

'''

# from bs4 import BeautifulSoup
# import requests

# Website se HTML content lena
# response = requests.get('https://www.example.com')

# HTML content ko BeautifulSoup se parse karna
# soup = BeautifulSoup(response.text, 'html.parser')
# soup = BeautifulSoup(response.text, 'lxml')
# soup = BeautifulSoup(response.text, 'html5lib')


#  bs4 ek class h py library me ye do se jada argument bhi le skta hai
#  lekin ham do argument commanly use karte hai .  
#  ek to html content aur doosra parser ye parser kayi ho skte hai 
#  jaise html.parser lxml.parser ya html5lib
#  beautifulSop ke kuch method hai




# get() :- ye specific tag elemnt ko dhoondhta hai 
# getAll() :-ye sabhi matching tag ya elements ko dhoondhta hai
# text :-tag ke ander ka content select karta hai . 
# get() :- ye tag ke attribute ko get karta hai 
# Check if h1 tag exists
# h1_tag = soup.find('h1')

# if h1_tag:
#     # Agar h1 tag milta hai, toh text print karo
#     print(h1_tag.text)
# else:
#     print("No <h1> tag found.")



# ================================================================================================


import requests
from bs4 import BeautifulSoup
thing = requests.get("http://www.youtube.com");
# print(thing.text) # to ye sara text print kar dega 
  
  
#    ab agar mujhe kisi specific tag ko select karna hi to 
#  bs4 ko import krna padega 


# soup = BeautifulSoup(thing.text , 'html.parser');
# h1 = soup.find('a')
# print(h1)




# ============================== GET REQUEST IN PYTHON ======================== 
# import requests
# req = requests.get("https://www.google.com" , 'html.parser')
# print(req.text)



# =================================POST req in python ===========================
 
#  ham request ke response ke liye liye only response.text() ya response.json() ka hi use kar skte hai 
#  jab hame kisi website se plain data milta hai to .text() method ka use kiya jata hai 
#  aur jab kisi website ya api se data json format m milta hai jo ki
#  usuaaly har api se json hi milta hai to ham response.json() karte hai
#  ye method automatically json response ko python data structure like list ya tuple me convert kar deta hai .


# .content:
#     Agar aapko raw binary content chahiye
#     (for example, images or files), toh aap .content
#     ka use karte hain. Yeh bytes return karta hai.

# .headers:
#     Yeh HTTP response ke headers 
# return karta hai. Headers ka use request/response ke additional 
# information ko check karne ke liye hota hai.
#  jaise content type  ,coockies , server details etc . 
 
 
 
 
#  POST REQUESTS KA USE TABKARTE HAI JAB HAME SERVER KO DATA SEND KARNA HOTA HAI 
#  AUR YE DATA MAINLY FORM SUBMISSON , LOGIN DETAILS ME USE HOTA HAI 
import requests
# data = {
#     "name" : "Prabhat",
#     "age"  : 18,
# }
'''
to m ye bolu ki python status code ko return karta h apppni hhtp request me 
ChatGPT said:
Ji haan, aap bilkul sahi keh rahe hain!

Python ka requests module status code ko return karta hai jab aap HTTP request (jaise POST, GET, etc.) bhejte hain. Jab aap server se request bhejte hain, toh server apne response ke saath ek HTTP status code bhejta hai, jo bataata hai ki request ko kaise process kiya gaya.
'''
# response = requests.post("https://reqres.in/api/users" ,  data=data)
# # Status code check karke request ka status handle karna
# if response.status_code == 200:  # Server ne 200 status code return kiya hai
#     print("Request successful!")
#     print("Response:", response.text)  # Server ka response print kar rahe hain
# elif response.status_code == 201:  # Agar server ne 201 return kiya, matlab naya resource create ho gaya
#     print("User registered successfully!")
#     print("Response:", response.text)
# else:
#     print(f"Request failed with status code: {response.status_code}") 
    
    #  status code koo handle karke req bhejna best practice mana jata hai . 
    
    
    



# ================Delete Req in python =====================




'''
Response Status Code:
200: Success. Resource successfully delete ho gaya.
204: Success, par server ne koi content return nahi kiya.
404: Resource not found. Jo resource delete karna chahte the, woh nahi mila.
5xx: Server error. Server ki taraf se koi problem hui.
'''

# import requests

# # DELETE request ke liye URL (example ke liye user ko delete karna hai)
# url = "https://reqres.in/api/users/2"  # Yeh user ID "2" ka resource delete karega

# # DELETE request bhejna
# response = requests.delete(url)

# # Status code check karke response handle karna
# if response.status_code == 200:  # Agar server ne 200 status code return kiya
#     print("User deleted successfully!")  # User ko successfully delete kar diya
# elif response.status_code == 404:  # Agar server ne 404 return kiya, matlab resource nahi mila
#     print("User not found!")
# else:
#     print(f"Request failed with status code: {response.status_code}")

#  is POORE CODE ME YE ERR AAAYEGI KI JAB ID 2 VALA USER
#  BANA HI NHI HAI TO USKO DELETE KAISE KAROGE TO 
#  PEHLE USER BNAO FIR DELETE KARO




 
