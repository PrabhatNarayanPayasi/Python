import pandas as pd
print(pd.__version__)

# isko chalane ke liye pip install pandas



'''

Virtual environment Python mein ek isolated environment hota hai jahan pe aap apne project ke liye dependencies (libraries, packages) install kar sakte hain bina system-wide Python installation ko affect kiye. Matlab, aap alag-alag projects ke liye alag-alag versions of libraries install kar sakte hain, aur ek project ka package dusre project ko interfere nahi karega.

Iska fayda yeh hai ki:

Dependency management: Agar aapko ek specific version of a package chahiye toh aap virtual environment bana sakte ho aur usmein woh version install kar sakte ho.
Clean environment: Aapke system Python ke libraries pe koi bhi changes nahi honge, aur aapka project clean aur separate rahega.
Portability: Agar aapke paas project hai aur aap usse kisi aur machine pe chalana chahte ho, toh aap easily dependencies ko list kar sakte ho aur environment replicate kar sakte ho.
Virtual environment kaise banaye:
Install virtualenv (agar aapke paas pehle se nahi hai):

bash
Copy
pip install virtualenv
Create a new virtual environment:

bash
Copy
python -m venv myenv
Yeh command myenv naam ka folder bana dega, jisme aapka isolated Python environment hoga.

Activate the virtual environment:

Windows pe:
bash
Copy
myenv\Scripts\activate
Mac/Linux pe:
bash
Copy
source myenv/bin/activate
Install packages: Aap jo bhi package install karna chahte hain, woh sirf iss environment mein hoga. Jaise:

bash
Copy
pip install numpy
Deactivate the environment: Jab kaam ho jaye, virtual environment ko deactivate karne ke liye:

bash
Copy
deactivate
Is tarah se aap apne Python projects ko better manage kar sakte ho.
'''