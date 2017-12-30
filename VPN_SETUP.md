# VPN SETUP

## Setup OpenVPN on a VPS (Ubuntu)

### Get a VPS with Ubuntu installed.
Update it
```bash
apt-get update
```
```bash
apt-get upgrade
```

### Setup OpenVPN by running this command
```bash
wget https://git.io/vpn -O openvpn-install.sh && bash openvpn-install.sh
```
Make sure to check if detected IP address is correct. After that you may just press enter to every question script asks.

### Find a config file for your VPN client
It should be in your home directory called something like client1.ovpn. Download it somewhere to your computer that you wish to connect through a VPN connection.

### Add a new clint that can use your VPN server
To create a new user go to your home directory where you downloaded openvpn-install.sh script and type
```bash
bash openvpn-install.sh
```
Then you should choose option "1" to create a certificate for a new user. Press Enter and then download this newly created certificate to clinet computer.

## Setup OpenVPN on Windows

### Download OpenVPN GUI client
[https://openvpn.net/index.php/open-source/downloads.html](https://openvpn.net/index.php/open-source/downloads.html)

Go through the setup process. Default install location will be C:\Program Files\OpenVPN

### Place *.ovpn file OpenVPN config folder
Default location of config folder is C:\Program Files\OpenVPN\config\

### Run OpenVPN GUI clinet
An icon should appear in your tray. Double click it and you should see it connecting to your VPS to aquire a VPN connection.
If OpenVPN is connected successuflly its tray icon should become green.

### Test your internet connection
Go to some website that allows you to check your IP adrres. Example: [https://ifconfig.co/](https://ifconfig.co/)

Your IP address shown on such site should be the same as your VPSs IP address.


## Setup OpenVPN on a Mac

### Download and install TunnelBlick
From [https://tunnelblick.net/](https://tunnelblick.net/) you can download an OpenVPN Gui client for Mac. Double click on a downloaded .dmg file and follow instructions.

### Download client certificate from VPN server
To download a client certificate that you've previously created (for example it's name is client1.ovpn) for your Mac type in terminal:
```bash
sftp server_user@server_IP:client1.ovpn ~/
```
This will download client1.ovpn to your Mac user home folder. 

### Connect to VPN server
To use client1.ovpn certificate you need to drag it to the top bar and drop it over TunnelBlick icon. Then click on TunnelBlick icon and choose "Connect client1"

### Test your internet connection
Go to some website that allows you to check your IP adrres. Example: [https://ifconfig.co/](https://ifconfig.co/)

Your IP address shown on such site should be the same as your VPSs IP address.
