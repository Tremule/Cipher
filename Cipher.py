#!/usr/bin/env python
import sys
import time
"""
This program will encode or decode a string of characters in accordance with the rules outlined in the key dictionary 
and ouput a newly create txt file with the encoded or decoded msg.
"""
key = {'a':'n', 'b':'o', 'c':'p', 'd':'q', 'e':'r', 'f':'s', 'g':'t', 'h':'u', 
       'i':'v', 'j':'w', 'k':'x', 'l':'y', 'm':'z', 'n':'a', 'o':'b', 'p':'c', 
       'q':'d', 'r':'e', 's':'f', 't':'g', 'u':'h', 'v':'i', 'w':'j', 'x':'k',
       'y':'l', 'z':'m', 'A':'N', 'B':'O', 'C':'P', 'D':'Q', 'E':'R', 'F':'S', 
       'G':'T', 'H':'U', 'I':'V', 'J':'W', 'K':'X', 'L':'Y', 'M':'Z', 'N':'A', 
       'O':'B', 'P':'C', 'Q':'D', 'R':'E', 'S':'F', 'T':'G', 'U':'H', 'V':'I', 
       'W':'J', 'X':'K', 'Y':'L', 'Z':'M'}

# Takes string of characters and converts to readable sentence      
def decode(key, msg):      
    result = []     
    msg_prep= list(msg)
    for i in msg_prep:
        if i in key.keys():
            result.append(key[i])
        else:
            result.append(i)

    return "".join(result)

#Takes a text and scambles it. 
def encode(key,msg):
    result = []
    msg_prep = list(msg)
    for i in msg_prep:
        if i in key.values():
            result.append(key.keys()[key.values().index(i)])
        else:
            result.append(i) 

    return "".join(result)

#retrieve file to process
def gettxt():
    command = raw_input("[I]mport file OR [T]ype in a string? >>")
    if command.lower() == "i":
        print "Which file do you want to import?"
        file = str(raw_input(">>  "))
        filename = open(file)
        return filename.read()

    elif command.lower() == "t":
        print "Please type the text you want to process"
        txt = raw_input(">> ")
        return txt
    else:
        print "Dafuq don't you understand?"
"""
Start program
"""
if __name__ == "__main__":
    
    print "Cipher_speak V.1\n"
    while True:
        try:
            print "\nChoose a command: \n"
            command = raw_input("\n[E]ncode\t[D]ecode\t[Q]uit >> ")
            if command.lower() == "e":
                msg = str(gettxt())
                new = open(raw_input('Name output file: '), 'a')
                new.write(encode(key,msg))
                new.close()
            elif command.lower() == "d":
                msg = str(gettxt())
                new = open(raw_input('Name output file: '), 'a')
                new.write(decode(key, msg))
                new.close()
            elif command.lower() == "q":
                print "cheers..."
                time.sleep(1)
                sys.exit()
            else:
                print "Invalid command, try again..."

        except:
            if command.lower() == "q":
                sys.exit()
            else:
                print "Something went wrong, try again"
                print "Make sure you add the file extension when importing.\n"
