import hashlib
import time
print ("                 ------------------------------------")
print ("                 --       Text To Md5 Hash  --")
print ("                 --                  By                --")
print ("                 --       @Mr_Amir_Typer   --")
print ("                 --                    |                 --")
print ("                 ------------------------------------")
print ("")
time.sleep(1)
k = input("[^] Your Text = ")
p = hashlib.md5(str(k).encode('utf-8')).hexdigest()
time.sleep(1)
print('''
[+] 25%   |===|''')
time.sleep(1)
print('''
[+] 50%   |=====|
''')
time.sleep(1)
print('''[-] 100%  |==========|
''')
time.sleep(2)
print("""-----------------------------------------
      """)
time.sleep(1)
print('''[*] Hashed :

''',"[*]",p)
print('')
time.sleep(2)
print('-----------------------------------------------------------')
time.sleep(1)
print ('''
[Bye Friend <3 | Script By @Mr_Amir_Typer]
''')
time.sleep(1)
print('-----------------------------------------------------------')

    
