
print('''
                     ~गोबिंद झा(GitHub: jha-git)
 _   _ ____  _   _ _   _ _____ _   _
| | | | __ )| | | | \ | |_   _| | | |
| | | |  _ \| | | |  \| | | | | | | |
| |_| | |_) | |_| | |\  | | | | |_| |
 \___/|____/ \___/|_| \_| |_|  \___/
                  ____ _   _ _____    _  _____ ____  _   _ _____ _____ _____
                 / ___| | | | ____|  / \|_   _/ ___|| | | | ____| ____|_   _|
                | |   | |_| |  _|   / _ \ | | \___ \| |_| |  _| |  _|   | |
                | |___|  _  | |___ / ___ \| |  ___) |  _  | |___| |___  | |
                 \____|_| |_|_____/_/   \_\_| |____/|_| |_|_____|_____| |_|
''')


ch = 'N'
while (ch == 'N' or ch == 'n' or query_no !=0):

    print("_________________________________MAIN MENU:___________________________________")
    print('''
             1. Privileges
             2. Network
             3. Display
             4. Special Packages
             5. System Services
             6. Firewall
             7. Package Management
             8. Application Names
             9. System
             0. Exit''' )
    print("______________________________________________________________________________")
    query_no=int(input("Enter Your Query:"))


    if query_no==1:
        print('''
 ____       _       _ _
|  _ \ _ __(_)_   _(_) | ___  __ _  ___  ___
| |_) | '__| \ \ / / | |/ _ \/ _` |/ _ \/ __|
|  __/| |  | |\ V /| | |  __/ (_| |  __/\__ \

|_|   |_|  |_| \_/ |_|_|\___|\__, |\___||___/
                             |___/

        ''')
        print('''
sudo command       #run command as root
sudo -s            #open a root shell
sudo -s -u user    #open a shell as user
sudo -k            #forget sudo passwords
gksudo command     #visual sudo dialog (GNOME)
kdesudo command    #visual sudo dialog (KDE)
sudo visudo        #edit /etc/sudoers
gksudo nautilus    #root file manager (GNOME)
kdesudo konqueror  #root file manager (KDE)
passwd             #change your password
         ''')
        exit_choice = input('Do You Want To Exit?Y/N: ')
        if exit_choice == 'Y' or exit_choice == 'y':
            query_no = 0
            ch = ''
        elif exit_choice  == 'N' or exit_choice  == 'n'  :
            ch = 'N'

    elif  query_no==2:
        print('''
 _   _      _                      _
| \ | | ___| |___      _____  _ __| | __
|  \| |/ _ \ __\ \ /\ / / _ \| '__| |/ /
| |\  |  __/ |_ \ V  V / (_) | |  |   <
|_| \_|\___|\__| \_/\_/ \___/|_|  |_|\_\
''')
        print('''
ifconfig                                #show network information
iwconfig                                #show wireless information
sudo iwlist scan                        #scan for wireless networks
sudo /etc/init.d/networking restart     #reset network for manual configurations
(file) /etc/network/interfaces          #manual configuration
ifup interface                          #bring interface online
ifdown interface                        #disable interface
        ''')
        exit_choice = input('Do You Want To Exit?Y/N: ')
        if exit_choice == 'Y' or exit_choice == 'y' :
            query_no = 0
            ch = ''
        elif exit_choice  == 'N' or exit_choice  == 'n'  :
            ch = 'N'


    elif  query_no==3:
        print('''
 ____  _           _
|  _ \(_)___ _ __ | | __ _ _   _
| | | | / __| '_ \| |/ _` | | | |
| |_| | \__ \ |_) | | (_| | |_| |
|____/|_|___/ .__/|_|\__,_|\__, |
            |_|            |___/

        ''')
        print('''
sudo /etc/init.d/gdm restart         #restart X and return to login (GNOME)
sudo /etc/init.d/kdm restart         #restart X and return to login (KDE)
(file) /etc/X11/xorg.conf            #display configuration
sudo dexconf                         #reset xorg.conf configuration
Ctrl+Alt+Bksp                        #restart X display if frozen
Ctrl+Alt+FN                          #switch to tty N
Ctrl+Alt+F7                          #switch back to X display
            ''')

        exit_choice = input('Do You Want To Exit?Y/N: ')
        if exit_choice == 'Y' or exit_choice == 'y':
            query_no = 0
            ch = ''
        elif exit_choice  == 'N' or exit_choice  == 'n'  :
            ch = 'N'



    elif  query_no==4:
        print('''
 ____                  _       _   ____            _
/ ___| _ __   ___  ___(_) __ _| | |  _ \ __ _  ___| | ____ _  __ _  ___  ___
\___ \| '_ \ / _ \/ __| |/ _` | | | |_) / _` |/ __| |/ / _` |/ _` |/ _ \/ __|
 ___) | |_) |  __/ (__| | (_| | | |  __/ (_| | (__|   < (_| | (_| |  __/\__ \

|____/| .__/ \___|\___|_|\__,_|_| |_|   \__,_|\___|_|\_\__,_|\__, |\___||___/
      |_|                                                    |___/


            ''')
        print('''
ubuntu-desktop              #standard Ubuntu environment
kubuntu-desktop             #KDE desktop
xubuntu-desktop             #XFCE desktop
ubuntu-minimal              #core Ubuntu utilities
ubuntu-standard             #standard Ubuntu utilities
ubuntu-restricted-extras    #non-free, but useful
kubuntu-restricted-extras   #KDE of the above
xubuntu-restricted-extras   #XFCE of the above
build-essential             #packages used to compile programs
linux-image-generic         #latest generic kernel image
linux-headers-generic       #latest build headers
            ''')

        exit_choice = input('Do You Want To Exit?Y/N: ')
        if exit_choice == 'Y' or exit_choice == 'y' :
            query_no = 0
            ch = ''
        elif exit_choice  == 'N' or exit_choice  == 'n'  :
            ch = 'N'



    elif  query_no==5:
        print('''
  ____            _                   ____                  _
/ ___| _   _ ___| |_ ___ _ __ ___   / ___|  ___ _ ____   _(_) ___ ___  ___
\___ \| | | / __| __/ _ \ '_ ` _ \  \___ \ / _ \ '__\ \ / / |/ __/ _ \/ __|
 ___) | |_| \__ \ ||  __/ | | | | |  ___) |  __/ |   \ V /| | (_|  __/\__ \

|____/ \__, |___/\__\___|_| |_| |_| |____/ \___|_|    \_/ |_|\___\___||___/
       |___/

            ''')
        print('''
start service                      #start job service (Upstart)
stop service                       #stop job service (Upstart)
status service                     #check if service is running(Upstart)
/etc/init.d/service start          #start service(SysV)
/etc/init.d/service stop           #stop service (SysV)
/etc/init.d/service status         #check service(SysV)
/etc/init.d/service restart        #restart service(SysV)
runlevel                           #get current runlevel

NOTE:   Use sudo to run these commands
            ''')
        exit_choice = input('Do You Want To Exit?Y/N: ')
        if exit_choice == 'Y' or exit_choice == 'y' :
            query_no = 0
            ch = ''
        elif exit_choice  == 'N' or exit_choice  == 'n'  :
            ch = 'N'

    elif query_no==6:
        print('''
 _____ _                        _ _
|  ___(_)_ __ _____      ____ _| | |
| |_  | | '__/ _ \ \ /\ / / _` | | |
|  _| | | | |  __/\ V  V / (_| | | |
|_|   |_|_|  \___| \_/\_/ \__,_|_|_|



        ''')
        print('''
ufw enable                 #turn on the firewall
ufw disable                #turn off the firewall
ufw default allow          #allow all connections by default
ufw default deny           #drop all connections by default
ufw status                 #current status and rules
ufw allow port             #allow traffic on port
ufw deny port              #block port
ufw deny from ip           #block ip adress

NOTE:   Use sudo to run these commands
         ''')

        exit_choice = input('Do You Want To Exit?Y/N: ')
        if exit_choice == 'Y' or exit_choice == 'y':
            query_no = 0
            ch = ''
        elif exit_choice  == 'N' or exit_choice  == 'n'  :
            ch = 'N'
    elif query_no==7:
        print('''
 ____            _
|  _ \ __ _  ___| | ____ _  __ _  ___
| |_) / _` |/ __| |/ / _` |/ _` |/ _ \

|  __/ (_| | (__|   < (_| | (_| |  __/
|_|   \__,_|\___|_|\_\__,_|\__, |\___|
                           |___/
 __  __                                                   _
|  \/  | __ _ _ __   __ _  __ _  ___ _ __ ___   ___ _ __ | |_
| |\/| |/ _` | '_ \ / _` |/ _` |/ _ \ '_ ` _ \ / _ \ '_ \| __|
| |  | | (_| | | | | (_| | (_| |  __/ | | | | |  __/ | | | |_
|_|  |_|\__,_|_| |_|\__,_|\__, |\___|_| |_| |_|\___|_| |_|\__|
                          |___/


        ''')
        print('''
apt-get update                  #refresh available updates
apt-get upgrade                 #upgrade all packages
apt-get dist-upgrade            #upgrade with package replacements;
                                 upgrade Ubuntu version
apt-get install pkg             #install pkg
apt-get purge pkg               #uninstall pkg
apt-get autoremove              #remove obsolete packages
apt-get -f install              #try to fix broken packages
dpkg --configure -a             #try to fix broken packages
dpkg -i pkg.deb                 #install file pkg.deb
(file) /etc/apt/sources.list    #APT repository list

NOTE:   Use sudo to run these commands
         ''')
        exit_choice = input('Do You Want To Exit?Y/N: ')
        if exit_choice == 'Y' or exit_choice == 'y':
            query_no = 0
            ch = ''
        elif exit_choice  == 'N' or exit_choice  == 'n'  :
            ch = 'N'
    elif query_no==8:
        print('''
    _                _ _           _   _
   / \   _ __  _ __ | (_) ___ __ _| |_(_) ___  _ __
  / _ \ | '_ \| '_ \| | |/ __/ _` | __| |/ _ \| '_ \

 / ___ \| |_) | |_) | | | (_| (_| | |_| | (_) | | | |
/_/   \_\ .__/| .__/|_|_|\___\__,_|\__|_|\___/|_| |_|
        |_|   |_|
 _   _
| \ | | __ _ _ __ ___   ___  ___
|  \| |/ _` | '_ ` _ \ / _ \/ __|
| |\  | (_| | | | | | |  __/\__ \

|_| \_|\__,_|_| |_| |_|\___||___/


        ''')
        print('''
nautilus         #file manager (GNOME)
dolphin          #file manager (KDE)
konqueror        #web browser (KDE)
kate             #text editor (KDE)
gedit            #text editor (GNOME)
         ''')

        exit_choice = input('Do You Want To Exit?Y/N: ')
        if exit_choice == 'Y' or exit_choice == 'y':
            query_no = 0
            ch = ''
        elif exit_choice  == 'N' or exit_choice  == 'n'  :
            ch = 'N'


    elif query_no==9:
        print('''
 ____            _
/ ___| _   _ ___| |_ ___ _ __ ___
\___ \| | | / __| __/ _ \ '_ ` _ \

 ___) | |_| \__ \ ||  __/ | | | | |
|____/ \__, |___/\__\___|_| |_| |_|
       |___/


        ''')
        print('''
Recovery -              Type the phrase “REISUB” while
                        holding down Alt and SysRq (PrintScrn) with
                        about 1 second between each letter. Your system
                        will reboot.
lsb_release -a          #get Ubuntu version
uname -r                #get kernel version
uname -a                #get all kernel information
         ''')

        exit_choice = input('Do You Want To Exit?Y/N: ')
        if exit_choice == 'Y' or exit_choice == 'y':
            query_no = 0
            ch = ''
        elif exit_choice  == 'N' or exit_choice  == 'n'  :
            ch = 'N'


    elif query_no == 0:
       exit()
