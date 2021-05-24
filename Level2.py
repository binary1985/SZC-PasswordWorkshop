import hashlib, sys

if len(sys.argv) < 3:
	print ("Usage is: " +sys.argv[0]+" <input hashlist> <input wordlist>")
	sys.exit()

with open(sys.argv[1], "r") as hash_file: # Open up the input hashlist in binary format
  hash_list = hash_file.read().splitlines() # Read the hashlist and form it into a list
  hash_file.close() # Close hashlist

with open(sys.argv[2], "rb") as word_file: # Open up the input wordlist in binary format
  word_list = word_file.read().splitlines() # Read the wordlist and form it into a list
  word_file.close()

for canidate in word_list: # Loop through the word_list list
    canidate_hash = hashlib.md5(canidate.strip()) # Convert word into MD5
    if canidate_hash.hexdigest() in hash_list: # Compare MD5 to entire hashlist
      print ("Found MD5:" + str(canidate_hash.hexdigest()) + ":" + str(canidate.decode("utf-8"))) # Print output, we need to encode the canidate
