import shutil
import os
from tkinter import *
from elevate import elevate

# Request Sudo Rights to Access Files for Backup
elevate(graphical=False)

# Locate USB
volume_list = os.listdir('/Volumes')

# Get user accounts from iMac
users = os.listdir('/Users')


def grabfiles(theuser, finalvol):
    # Get Current Working Directory
    cur_dir = os.getcwd()

    # Get current path the script is running from (Jump Drive)
    full_cur_dir_path = finalvol + """/""" + theuser
    print(full_cur_dir_path)

    # Count Files On Documents
    documents = '/Users/' + str(theuser) + '/Documents'
    os.chdir(documents)
    documents_count = sum([len(files) for r, d, files in os.walk(documents)])
    print(documents_count)
    documents_label.configure(text=('Documents Count: ' + str(documents_count)))

    # Count Files On Downloads
    downloads = '/Users/' + str(theuser) + '/Downloads'
    os.chdir(downloads)
    downloads_count = sum([len(files) for r, d, files in os.walk(downloads)])
    print(downloads_count)
    downloads_label.configure(text=('Downloads Count: ' + str(downloads_count)))

    # Count Files On Desktop
    desktop = '/Users/' + str(theuser) + '/Desktop'
    os.chdir(desktop)
    desktop_count = sum([len(files) for r, d, files in os.walk(desktop)])
    print(desktop_count)
    desktop_label.configure(text=('Desktop Count: ' + str(desktop_count)))

    # Make Username Directory to Store Files In.
    os.chdir(finalvol)
    if not os.path.exists(finalvol + "/" + theuser):
        os.mkdir(theuser)

    # os.system("""sudo chown -R """ + current_user + """ /Users/""" + username)

    # Documents
    os.system("""sudo cp -r /Users/""" + str(theuser) +
              """/Documents '""" + str(full_cur_dir_path) + """'""")
    # Downloads
    os.system("""sudo cp -r /Users/""" + str(theuser) +
              """/Downloads '""" + str(full_cur_dir_path) + """'""")
    # Desktop
    os.system("""sudo cp -r /Users/""" + str(theuser) +
              """/Desktop '""" + str(full_cur_dir_path) + """'""")

    # Change File Permissions
    os.system("""sudo chmod -R 770 '""" + full_cur_dir_path + """'""")

    # Open the backup location for the user.
    os.system("""open '""" + full_cur_dir_path + """'""")

    listbox_vol.configure(selectbackground="#18a104")
    listbox.configure(selectbackground="#18a104")


# Execute backup fuction

window = Tk()

window.title("NBackup")
window.resizable(width=False, height=True)

def clicked():
    grabfiles(picked_user, picked_vol)

label = Label(window, text="Backup Location")
labeluser = Label(window, text="User Folder")
listbox_vol = Listbox(window, width=45, selectmode=SINGLE, bd=0, bg='#222', fg='#fff', selectforeground='#fff', selectbackground="#064fd6", activestyle='none', exportselection=False)
listbox = Listbox(window, width=45, selectmode=SINGLE, bd=0, bg='#222', fg='#fff', selectforeground='#fff', selectbackground="#064fd6", activestyle='none')
button = Button(window, text="Backup", width=30, height=2, command=clicked)
documents_label = Label(text='Documents Count:')
downloads_label = Label(text='Downloads Count:')
desktop_label = Label(text='Desktop Count:')

label.grid(column=0, columnspan=1, row=0, padx=5, ipadx=5, ipady=5)
labeluser.grid(column=1, columnspan=1, row=0, padx=5, ipadx=5, ipady=5)
listbox_vol.grid(column=0, row=1, padx=5, ipadx=5, ipady=5)
listbox.grid(column=1, row=1, padx=5, pady=5, ipadx=5, ipady=5)
button.grid(column=0, columnspan=1, row=3, rowspan=3, padx=5, pady=5)
documents_label.grid(column=1, row=3)
downloads_label.grid(column=1, row=4)
desktop_label.grid(column=1, row=5)

# Add Volumes to Listbox_vol
listbox_vol.delete(0, 'end')
i = 0
for vol in volume_list:
    listbox_vol.insert(i, vol)
    i = i + 1

# Add User Accounts to Listbox
listbox.delete(0, 'end')
i = 0
for user in users:
    listbox.insert(i, user)
    i = i + 1


def callbackVol(event):
    global picked_vol
    selection = event.widget.curselection()
    if selection:
        index = selection[0]
        picked_vol = event.widget.get(index)
        listbox_vol.configure(selectbackground="#064fd6")
        print(picked_vol)
        picked_vol = "/Volumes/" + picked_vol
        label.configure(text="Backup Location: " + picked_vol)
        return picked_vol


def callbackName(event):
    global picked_user
    selection = event.widget.curselection()
    if selection:
        index = selection[0]
        picked_user = event.widget.get(index)
        listbox.configure(selectbackground="#064fd6")
        labeluser.configure(text="User Folder: " + picked_user)
        print(picked_user)

        # Count Files On Documents
        documents = '/Users/' + str(picked_user) + '/Documents'
        os.chdir(documents)
        documents_count = sum([len(files) for r, d, files in os.walk(documents)])
        print(documents_count)
        documents_label.configure(text=('Documents Count: ' + str(documents_count)))

        # Count Files On Downloads
        downloads = '/Users/' + str(picked_user) + '/Downloads'
        os.chdir(downloads)
        downloads_count = sum([len(files) for r, d, files in os.walk(downloads)])
        print(downloads_count)
        downloads_label.configure(text=('Downloads Count: ' + str(downloads_count)))

        # Count Files On Desktop
        desktop = '/Users/' + str(picked_user) + '/Desktop'
        os.chdir(desktop)
        desktop_count = sum([len(files) for r, d, files in os.walk(desktop)])
        print(desktop_count)
        desktop_label.configure(text=('Desktop Count: ' + str(desktop_count)))
        return(picked_user)


listbox_vol.bind("<<ListboxSelect>>", callbackVol)

listbox.bind("<<ListboxSelect>>", callbackName)
# window.configure(background="#000")
window.mainloop()
