### PasswordCracker

## Part 1
The password file (shadowfile.txt) was generated with creation of 200 users (crack01—crack200)
with password taken from random English dictionary words and some commonly used passwords.
We downloaded a dictionary file from the Internet, named commonPasswdFile.txt, containing
about 100,000 entries. You should be able to find similar dictionary files by searching in Internet.
The password file contains for each user: username, salt, hashed password, and some more details.

# Goals

The goals in this problem are to do the following activities:
a. List all the attributes that are stored for an individual user in a shadow file.
b. Where do the passwords in Windows system get stored?
c. A Python program (must be well documented) that uses the commonPasswdFile.txt and
compute the necessary hash of the passwords to compare them with the passwords stored
in shadow file.
• The program should output all the username:password combinations after successful
crack. Please list all the cracked combinations in the report.

## Part 2

imagine you have 500 password hashes from a password database of a web service
(extracted to the file “UnsaltedPassTable.txt”). Assume that the users are not really familiar with
password security and create their passwords in the following ways:
1. An English word as the password (e.g. “secret”)
2. A string of up to 8-digits as password (e.g. “87654321”)
3. An English word followed by some digits, but together no more than 10 characters (e.g.
password89)
4. Concatenate two English words together (e.g. “secretpassword”)

## Part 3
Imagine, you got access to another password table from the same web server, but this contains
usernames and password of 100 VIP users (extracted to the file “SaltedPassTable.txt”). The
website has SALTED the password hashes to provide better security, however the users still
created their passwords based on same way as discussed above. There are only 100 password
hashes in this table, and the salt values are provided alongside the hashes.

# Goals

The goals in the above two problems is to
a. Find all the cracked passwords.
b. Report the time taken to crack for all the users and provide your remarks on why they are
different.
