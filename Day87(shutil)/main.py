# pip install shutil
#  ye [ython 3.8 ke baad introduce hua hai iska 
#  main paurpose file operations jo hote hai jaise ki copying moving renaming deleting etc . 
# in operations ko  karte hai shutil module ke help se . 
#  ye module file system ko manage karne ke liye use hota hai . 

#  there are some functions which are used in shutil module
# shutil.copy() : it is used to copy file fron one location to another 
#  shutil.move() : it is used to move file from one to another location
#  shutil.rmtree() : ek directory ko uske content ke sath recursivly delete karne ke liye use kiya jata hai .
#  shutil.disk_usags() : Disk ka usesage jaise ki free aur used space dikhane ke liye 
# shutil.make_archive() : file ko archive ya zip karne ke liye .
# shutil.unpack_archive() : Archived file ya zipped file ko extract bnane ke liye .


# 1. shutil.copy(src, dst)
# Is function ka use ek file ko ek location se doosri location par copy karne ke liye kiya jaata hai.
 
# shutil.copy(src, dst)
# src: Yeh source file ka path hota hai, jise aap copy karna chahte hain.
# dst: Yeh destination ka path hota hai, jahan par file ko copy karna hai.


'''
2. shutil.move(src, dst)
Iska use kisi file ya folder ko ek jagah se doosri jagah move karne ke liye hota hai. Agar destination mein file pehle se maujood hai, toh wo overwrite ho jaati hai.
 
shutil.move(src, dst)
src: Yeh file ya directory jo aap move karna chahte hain.
dst: Yeh destination ka path hai.
'''


'''
3. shutil.rmtree(path)
Iska use ek directory ko uske contents ke saath recursively delete karne ke liye hota hai.
Isse sub-directories aur files bhi delete ho jaati hain.
  file delete karne ke liye shutil ka use nnhi kar skte iske liye hame 
  os.remove karna padega.
shutil.rmtree(path)
path: Yeh wo directory hai jo aap delete karna chahte hain.
'''




import shutil
# shutil.copy("C:\Users\prabh\.vscode\Python\Day87(shutil)\main.py" , "C:\Users\prabh\.vscode\Python\Day87(shutil)\main2.py")
# shutil.move('Day87(shutil)/main.py' , 'main.py')
