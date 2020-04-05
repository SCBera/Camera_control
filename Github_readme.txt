***To configure new PC for githun communication***

# set git user name
git config --global user.name "SCBera"
#check the username
git config --global user.name
> SCBera
# set git email
git config --global user.email "email@example.com"
#check the email
git config --global user.email


# To generate id_rsa etc...for every new PC it may require.
ssh-keygen -t rsa -C subhas.9874@gmail.com
>Generating public/private rsa key pair.
>Enter file in which to save the key (/c/Users/subha/.ssh/id_rsa):
>Enter passphrase (empty for no passphrase):
>Enter same passphrase again:
>Your identification has been saved in /c/Users/subha/.ssh/id_rsa.
>Your public key has been saved in /c/Users/subha/.ssh/id_rsa.pub.
>The key fingerprint is:
>SHA256:9YHjQZIh6lo+ymsGXWL/A/84G1DNwKciWU11OYpG1CI subhas.9874@gmail.com
>The key's randomart image is:
+---[RSA 2048]----+
|     ==o+oo.     |
|    E.==++o.     |
|   o.o.=o.=..    |
|  =.o.+ .o + .   |
| o =+o  S . .    |
|. .+o.           |
| .. o+.          |
| .o. .=o         |
| o+.  o=.        |
+----[SHA256]-----+

# start the ssh agent....


#copy the ssh key containt
clip < ~/.ssh/id_rsa.pub

# go to settings to github page and then ssh and GPG keys then add new SSH and paste the key copied above

# add existing repository to github
-create a new repositorty in github and copy the url
-in git bash move to the repository and 
git remote add origin "copied url (without "")"

# For copying folder/directory from github
git clone 'copy and paste the url from github'
