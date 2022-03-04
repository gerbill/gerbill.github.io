# Squid Proxy Server Setup Steps


## (Optional) Update fresh Ubuntu installation
```bash
sudo apt update
sudo apt upgrade -y
```

## Install Squid and Apache2 Utils
```bash
sudo apt install squid apache2-utils -y
```
After installation Squid proxy is already running, but will deny all outbound connections by default.


## Set up proxy user authentication
Create a password file
```bash
sudo touch /etc/squid/passwd
```
Create a user named `gerbill` (you can name this user whatever you want)
```bash
sudo htpasswd /etc/squid/passwd gerbill
```
This command will prompt you to enter a password for this user twice. 
Any password will do, but **be aware - bots are constantly scanning for missconfigured or weakly protected proxy servers to use them for shady things later. Make sure to use a strong password!**  

Open `squid.conf` in your editor of choice. I'm using `nano`
```bash
sudo nano /etc/squid/squid.conf
```
Right at the top of `squid.conf` above the `#  WELCOME TO SQUID ....` line paste in the following 3 lines
```
auth_param basic program /usr/lib/squid/basic_ncsa_auth /etc/squid/passwd
acl squid_users proxy_auth REQUIRED
http_access allow squid_users
```
Save changes to `squid.conf` and restart Squid server for the changes to take effect
```bash
service squid restart
```

## Allow outbound connections
Search for `http_access deny all` inside `squid.conf` and change this line to `http_access allow all`.
Save changes to `squid.conf` and restart Squid server for the changes to take effect
```bash
service squid restart
```

## (Optional) Change default port
Squid server listens to `3128` port by default. You may change this port in order to further enhance your proxy server's security.  
Once again open up `squid.conf` in an editor and find a line that contains `http_port 3128`. Edit the default port number `3128` to, for example `8765` or whichever port number you like.   
Save changes to `squid.conf` and restart Squid server for the changes to take effect
```bash
service squid restart
```
