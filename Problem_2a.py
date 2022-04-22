import hashlib

users_passwords = [[]]

#gets a list of words from words.txt eliminating words <= 5 character
def valid_words (words):
    content = words.read()
    co_list = content.split("\n")

    co_list = sorting(co_list)

    new_word_list = []
    for i in range(len(co_list)): 
        if (len(co_list[i]) > 5):
            new_word_list.append(co_list[i])
    return new_word_list

#gets a list of hashed lines from shadowfile
def list_of_hash_lines(unsalted_passwords):
    content = unsalted_passwords.read()
    co_list = content.split("\n")
    return co_list

#gets the hashed password
def get_hash(line):
    return line.split(':')[1]

#gets the name of the user
def get_user(line):
    return line.split(':')[0]

#hashed a words
def hash(word):
    word = str(word)
    return (hashlib.md5(word.encode())).hexdigest() 

#removes list of alreday found passwords
def update_list (hash_line , hash_line_list):
    list = hash_line_list.remove(hash_line)
    return list
    
    #Instead of removing, adds it to a different list
def update_list(new_hash_list, hash_line_list):
    for i in range(len(new_hash_list)):
        hash_line_list.remove(new_hash_list[i])
    
    return hash_line_list

#sorts
def sorting(list):
    list = sorted(list, key=len)
    return list

#finds passwords with single word
def single_word(hash_line_list, word_list):
    new_hash_list = []

    for i in range(len(hash_line_list)):
        for j in range(len(word_list)):

            #gets value
            word = word_list[j]
            hashed_password = get_hash(hash_line_list[i])

            #if password found, its prints it with the username, password, and hash
            if (hash(word) == hashed_password):
                print(get_user(hash_line_list[i]), word, hash(word) ,hashed_password)

                #adds hashline to a list of found hashed password to later update the list of hashed_list and improve complexity
                new_hash_list.append(hash_line_list[i])

                #adds it to a list of found passwords
                list = [get_user(hash_line_list[i]), word, hash(word) ,hashed_password]
                users_passwords.append(list)

    return update_list(new_hash_list, hash_line_list)

#finds passwords with digits
def digits (hash_line_list):
    number = 9999999
    new_hash_list = []

    for i in range (len(hash_line_list)):
        while (number < 99999999):
            
            #if password found, its prints it with the username, password, and hash
            if (hash(number) == get_hash(hash_line_list [i])):
                print(get_user(hash_line_list[i]), number, hash(number), get_hash(hash_line_list[i]))

                #adds hashline to a list of found hashed password to later update the list of hashed_list and improve complexity
                new_hash_list.append(hash_line_list[i])
                
                #adds it to a list of found passwords
                list = [get_user(hash_line_list[i]), number, hash(number) ,get_hash(hash_line_list[i])]
                users_passwords.append(list)

            #resets values
            number += 1
        number = 9999999

    return update_list(new_hash_list, hash_line_list)

#An English word followed by some digits, but together no more than 10 characters (e.g. password89)
def english_with_digits(hash_line_list, word_list):
    new_hash_list = []
    number = 0
    password = ''

    for i in range(len(hash_line_list)):
        for j in range(len(word_list)):
            while(len(password) < 11):

                #gets value
                password = word_list[j]
                password = password + (str(number))

                #if password found, its prints it with the username, password, and hash
                if (hash(password) == get_hash(hash_line_list[i])):
                    print(get_user(hash_line_list[i]), password, hash(password), get_hash(hash_line_list[i]))

                    #adds hashline to a list of found hashed password to later update the list of hashed_list and improve complexity
                    new_hash_list.append(hash_line_list[i])

                    #adds it to a list of found passwords
                    list = [get_user(hash_line_list[i]), password, hash(password) ,get_hash(hash_line_list[i])]
                    users_passwords.append(list)

                #resets values
                number = int(number)
                number += 1
            number = 0
            password = ''

    return update_list(new_hash_list, hash_line_list)

def concatenate_words(hash_line_list, word_list):
    new_hash_list = []

    for i in range (len(hash_line_list)):   
        for j in range(len(word_list)):
            for z in range (len(word_list)):

                #gets Values
                password = (word_list[j] + word_list[z])

                #if password found, its prints it with the username, password, and hash
                if (hash(password) == get_hash(hash_line_list[i])):
                    print(get_user(hash_line_list[i]), password, hash(password), get_hash(hash_line_list[i]))

                    #adds hashline to a list of found hashed password to later update the list of hashed_list and improve complexity
                    new_hash_list.append(hash_line_list[i])

                    #adds it to a list of found passwords
                    list = [get_user(hash_line_list[i]), password, hash(password) ,get_hash(hash_line_list[i])]
                    users_passwords.append(list)

    return update_list(new_hash_list, hash_line_list)

def main():
    with open ('unsaltedPassTable.txt') as unsalted_passwords, open('words.txt') as words:
        word_list = valid_words(words)
        hash_line_list = list_of_hash_lines(unsalted_passwords)

        #Finished
        hash_line_list = single_word(hash_line_list, word_list)
        hash_line_list = english_with_digits(hash_line_list, word_list)
        hash_line_list = digits(hash_line_list)
        hash_line_list = concatenate_words(hash_line_list, word_list)
                            
        
        #writes answers to text file
        file = open ("/Answers/2a_passwords.txt", "x")
        for i in range(len(users_passwords)):
            file.write(str(users_passwords[i]))

if __name__ == "__main__":
    main()
   

