#checks for all the passwords for all the usernames

from crypt import crypt

#gets a list of hashed lines from shadowfile
def list_of_hash_lines(shadowfile):

    content = shadowfile.read()
    co_list = content.split("\n")

    new_list = []
    for i in range(len(co_list)):
        if (i > 1):
            new_list.append(co_list[i])
    return new_list

#turns commonPasswdFile into list
def list_of_words(commonPasswdFile):
    content = commonPasswdFile.read()
    co_list = content.split("\n")
    return co_list

#gets the hash
#$1$8gHe0C.s$1Erf75Zrde3V1babmlbUU1
def get_hash(line):
    return line.split(':')[1]

#gets the hashed password
#$1Erf75Zrde3V1babmlbUU1
def get_hashed_password(line):
    return line.split('$')[3]

#gets the salt
#$1$l3RgvDgR
def get_salt(line):
    salt = '$'
    salt += line.split('$')[2]
    return salt

#returns the username
def get_user(line):
    return line.split(':')[0]

#hashed a words
def hash(word, salt):
    word = str(word)
    #return  (hashlib.md5(salt.encode() + word.encode()).hexdigest()) #doesn't work
    return crypt(word, salt)#doesn't work?

#search throuhout entire word list and all hashes fr passwords
def find_password(hash_line_list, word_list):
    for i in range(len(hash_line_list)):
        for j in range (len (word_list)):
            
            word = word_list[j] # gets word from commonPasswdFile
            hashed_line = get_hash(hash_line_list[i]) #gets the hash line of shadowfile
            #hashed_password = get_hashed_password(hashed_line) #gets the hashed password from the line from shadowfile
            salt = get_salt(hashed_line) #gets the salt from the line from shadowfile

            #print(hash(word,salt), ('$' + hashed_password))
            if (hash(word, salt) == hashed_line): #checks if the hash of the word plus the salt is equal to
                print(get_user(hashed_line), ':', word)      #the hashed_password from the line of shadowfile

def main():
    with open('shadowfile.txt') as shadowfile, open ('commonPasswordFile2.txt') as commonPasswdFile:
        hash_line_list = list_of_hash_lines(shadowfile)
        word_list = list_of_words(commonPasswdFile)

        #find_password(hash_line_list, word_list)

        password = '123456'
        hashed_password = ".jp4EA47X38Yny8reSbi71"
        salt = "$1$l3RgvDgR$"

        password = crypt(password, salt)
        print(password, hashed_password)



if __name__ == "__main__":
    main()
