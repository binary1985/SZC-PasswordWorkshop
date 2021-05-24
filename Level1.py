import hashlib

hash = '2ac9cb7dc02b3c0083eb70898e549b63' #This is our target hash Password1

with open("rockyou.txt", "rb") as a_file: # Open the file read only in binary format
  for line in a_file: # Loop through the file
    testhash = hashlib.md5(line.strip()) # Generate MD5 hash on word
    if testhash.hexdigest() == hash: #Compare MD5 hash to target hash
      print ("Found: " + hash + ":" + line.decode('ascii').strip()) # Print results
      break # Quit so we dont process the whole file
