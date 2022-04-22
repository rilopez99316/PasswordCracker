## PasswordCracker

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
