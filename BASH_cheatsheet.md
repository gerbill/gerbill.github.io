## BASH useful commands

##### Create a sudo user
Log in as root.  
Set and confirm the new user’s password at the prompt. A strong password is highly recommended!
```bash
adduser some_username
```
Use the usermod command to add the user to the sudo group.
```bash
usermod -aG sudo some_username
```
Use the su command to switch to the new user account.
```bash
su - some_username
```
Once logged in as some_username test out your sudo privileges by installing Midnight Commander!
```bash
sudo apt install mc
```

##### Create a text file with no duplicate lines
```bash
sort input.txt | uniq > output.txt
```

##### Count lines in file
```bash
wc -l filename.txt
```

##### Archive a folder with TAR
```bash
tar -zcvf foldername.tar.gz foldername_tocompress
```

##### UnTAR an archive
```bash
tar -xf archive.tar -C /target/directory
```

##### Get directory size
```bash
du -hs /path/to/directory
```

##### Find a file without permission dinied errors
```bash
find /home/projects/ -name "*part_of_a_filename*"  2>&1 | grep -v "Permission denied"
```

##### Find a specific text inside files
```bash
grep -Ril "text-to-find-here" /path/to/folder/where/to/search
```

##### Set up RDP on a new Ubuntu VPS
Create rdp.sh file
```bash
nano rdp.sh
```
Copy and paste this code in rdp.sh
```bash
apt-get update
apt-get upgrade -y
apt install mc -y
apt install htop -y
apt install xfce4 xfce4-goodies xorg dbus-x11 x11-xserver-utils -y
apt install xrdp -y
systemctl status xrdp
adduser xrdp ssl-cert
echo "address=0.0.0.0" >> /etc/xrdp/xrdp.ini
apt-get install gnome-icon-theme-full tango-icon-theme
echo xfce4-session >~/.xsession
systemctl restart xrdp
```
Run rdp.sh using command
```bash
source rdp.sh
```
Don't go far, you will see a pink confirmation screen. Just hit ENTER when you see it
