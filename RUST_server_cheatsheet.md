# RUST SERVER CHEATSHEET

## Installation

These Rust Linux Server installation instructions are for Ubuntu 16.04 64-bit server (should probably work for Ubuntu version 12.04 or greater)

#### System requirements
* RAM: 6 - 12GB
* CPU: Choose CPU with most performace per each core. No point in many cores. A CPU with 4 powerful cores (3.5 - 4.5 Ghz) would work the best.
* Bandwidth: 100 Mb/s should work fine. Ping should be minimal tho.
* Hard drives: SSD is the only option for best performance.

#### Install Dependencies
```bash
sudo dpkg --add-architecture i386; sudo apt-get update;sudo apt-get install mailutils postfix curl wget file bzip2 gzip unzip bsdmainutils python util-linux ca-certificates binutils bc tmux lib32gcc1 libstdc++6 libstdc++6:i386 lib32z1
```
You may be asked to choose a mail server configuration. Choose "No configuration"

#### Rust Server User
Create a user with password to run steam-realated and rust-related stuff. Running this stuff under root is a security risk!
```bash
adduser rustserveruser
```
You will be asked what password to set. Its always best to use strong password! Other questions may be skipped by pressing ENTER.

Login with this newly created user
```bash
su rustserveruser
```
Change to this user home directory
```bash
cd ~
```

#### Download and run LGSM script
```bash
wget -N --no-check-certificate https://gameservermanagers.com/dl/linuxgsm.sh && chmod +x linuxgsm.sh && bash linuxgsm.sh rustserver
```

#### Run the installer and follow the instructions
```bash
./rustserver install
```
When it'll ask you about Server Directory - just hit ENTER

When it'll ask you "Was the install successufl" - hit ENTER

### Editing config files
#### Edit common.cfg
Once installation is complete we have to change 2 cfg files with our settings

Go to lgsm config directory
```bash
cd /home/rustserveruser/lgsm/config-lgsm/rustserver
```
Copy default config to common.cfg
```bash
cp _default.cfg common.cfg
```
Now edit this common.cfg using nano editor
```bash
nano common.cfg
```
Now look through the lines under "Server Settings" header and change what you want. 
* First of all you want to change ip address from 0.0.0.0 to the ip address of your Ubuntu Linux server. 
* Then you must edit the password at a setting named "rconpassword".
* Then you probably want to change Rust server title from "Rust" to "Your Awesome Server Name or Smth".
* And change "maxplayers" if the default setting isn't enough for you.

The default map is "Procedural Map". If you want to change it to "HapisIsland" for example, you have to do the following:
* In the common.cfg file find "Server Start Command" header.
* There you will see some thing like "+server.ip ${ip} +server.port ${port}" and so on. A long line like this.
* Between "+server.ip ${ip}" and "+server.port ${port}" add the following:
```bash
+server.level "HapisIsland"
```

Once you've done editing common.cfg you need to save your changes by pressing Ctrl+O and then hitting ENTER. To quit nano editor type Ctrl+X

Now change directory to where server.cfg file located
```bash
cd /home/rustserveruser/serverfiles/server/rustserver/cfg
```
And edit it with nano editor
```bash
nano server.cfg
```
Here you want to edit the following:
* Change default server description to what you need. Defaul server description is in the quotes and starts like "This is the defaul LinuxGSM server...". Change it you your liking. Use \n for new lines.
* Edit server header image to a link of an image for your server (instead of a default link that starts with "https://raw.githubusercontent.com...".
* Edit your server website.

Once done editing again type Ctrl+O to save the file and Ctrl+X to exit nano.

#### Running the Rust Server
Change to rustserveruser home directory
```bash
cd ~
```
And finally start the server
```bash
./rustserver start
```
If everything is fine you should see the following:
```bash
[  OK  ] Starting rustserver: YourServerTitle
```

#### Log in to your server
* log in to your Steam account in the Steam app
* run Rust game
* open console by pressing F1
* in the console type (in this example I used 207.154.240.244 IP and 28015 port. You will have different IP. Port should still be 28015 unless you changed it in common.cfg)
```bash
client.connect 207.154.240.244:28015
```












