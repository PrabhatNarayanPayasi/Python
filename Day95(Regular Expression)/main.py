import re
pattern = r'hello';
text = "hello world , hello bhai  , Hello mittr , HELLO Brother";
# resulte = re.search(pattern , text);ye first occurance ko hi return kar deta hai
# matlb jaha se match o gya vahi return kar diya 

# resulte = re.findall(pattern , text)
#  ye poori string me sabhi occurance ko return karta hai 
#  start se leke end tak jitne bhi hai sabhi ko return karta hai 
#  inka type tuple hota hai 
resulte = re.sub(pattern , "OK" , text)
#  ye substitute karta hai string ko jis naam se ham replace 
#  karna chahte hai . 
 
if resulte:
    print(f"Found {resulte}");
else:
    print("Not")
    
    '''
    Regular expression (regex) ek pattern matching technique hoti hai jo strings ke andar specific patterns ko search karne ke liye use hoti hai. Python mein regex ka use karne ke liye re module ka use kiya jata hai.

Regular expression ke through hum strings mein specific patterns ko find, match, replace, ya validate kar sakte hain. Yeh kaafi powerful tool hai jo data extraction, validation, aur transformation ke kaam aata hai.

Python mein regex ko use karne ke liye sabse pehle re module ko import karna padta hai.
    '''




'''
matlb regular expression ka use    string mpattern ko find karne ke liye kiya jata hai 


ChatGPT said:


Haan, regular expression (regex) ka use strings mein specific patterns ko find, match, aur manipulate karne ke liye kiya jata hai. Regex ek pattern-based search aur match mechanism hai jo aapko string ke andar complex patterns ko efficiently search karne, extract karne, replace karne, aur validate karne ki suvidha deta hai.
Regular Expression ka Basic Use
Jab aapko kisi string mein kuch specific pattern search karna ho, jaise ki:

Email address,
Phone number,
Date,
Specific words ya numbers,
Text formatting check (jaise capital letters, small letters, digits etc.)
'''