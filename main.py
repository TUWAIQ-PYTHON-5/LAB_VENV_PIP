from art import *


art_1 = art("coffee") # return art as str in normal mode
print(art_1)

art_2=art("woman",number=2) # return multiple art as str
print(art_2)

Art=text2art("BELIEVE and ACHEIVE") # Return ASCII text (default font) and default chr_ignore=True 
print(Art)


Art=text2art("Python",font='block',chr_ignore=True) # Return ASCII text with block font
print(Art)
