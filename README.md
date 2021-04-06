# macbackup
Backup Mac User Profiles Easy

This app can be compiled with pyinstaller but I've attached the ZIP in hopes
you can copy and run it without building.

It was built on Catalina so it will work on MacOS versions newer than that,
up to Big Sur at least. 

You must enter an admin password to elevate your privalges to copy
another users folder at the start, then the UI will load.

Here is a link to the backup app.

https://github.com/BrainHurts/macbackup/raw/master/backup.zip 

Extract and run the contained app.

Running the app:
 1. a terminal will pop up that requires you enter the password of the currently logged in user, must be an admin
 2.  after the app loads pick a backup location from list or browse to it with the browse button
 3.  pick a user account from the list
 4.  verify at the top above both lists that the right backup location and user account are selected
 5.  hit backup

When done both selections will turn from blue to green and will open the location of the backup in a finder window.

This app will copy the desktop, documents, and downloads folder of the selected user.

It's also important to note that it will change the permissions of the files in the new backup location so that anyone can view, read, and write to those files.
