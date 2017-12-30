# SETUP A VPN ON A VPS

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


