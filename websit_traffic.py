#<-----Rathin--->
import webbrowser
import time
from pykeyboard import PyKeyboard

count=0
urls=['https://github.com/meliodas-123','https://www.codechef.com/users/rathin_r']
k=PyKeyboard()

while count<100:
   for url in urls:
      webbrowser.open(url,new=0)
      time.sleep(10)
      k.press_keys([k.windows_l_key,'d'])
      count=count+1
      

else:
  pass