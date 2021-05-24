import sys, os

if len(sys.argv) < 3: # Check for Argument Length
        print ("Usage is: " +sys.argv[0]+" <input hashlist> <input wordlist>") #Print Help
        sys.exit() #Exit 

os.system('hashcat -a 0 -m 0 ' + sys.argv[1] + ' ' + sys.argv[2]) # Check hashes for MD5
os.system('hashcat -a 0 -m 900 ' + sys.argv[1] + ' ' + sys.argv[2]) # Check hashes for MD4
os.system('hashcat -a 0 -m 1000 ' + sys.argv[1] + ' ' + sys.argv[2]) # Check hashes for NTLM

###Print Pretty
print (" ")
print (" ")
print (" ")
print (" ")
print (" ")
print (" ")
print (" ")
print ("----------------------------")
print (" Printing any Hashes Found:")
print ("----------------------------")
os.system('hashcat -a 0 -m 1000 ' + sys.argv[1] + ' --show')
print ("----------------------------")