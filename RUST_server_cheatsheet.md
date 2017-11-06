# RUST SERVER WITH MODS INSTALLATION AND MANAGEMENT

![Rust Server Installation Guide](https://i.imgur.com/6yl50jl.jpg)

These Rust Linux Server installation instructions are for Ubuntu 16.04 64-bit server (should probably work for Ubuntu version 12.04 or greater)

## System requirements
* RAM: 6 - 12GB
* CPU: Choose CPU with most performace per each core. No point in many cores. A CPU with 4 powerful cores (3.5 - 4.5 Ghz) would work the best.
* Bandwidth: 100 Mb/s should work fine. Ping should be minimal tho.
* Hard drives: SSD is the only option for best performance.

## Install Dependencies
```bash
sudo dpkg --add-architecture i386; sudo apt-get update;sudo apt-get install mailutils postfix curl wget file bzip2 gzip unzip bsdmainutils python util-linux ca-certificates binutils bc tmux lib32gcc1 libstdc++6 libstdc++6:i386 lib32z1
```
You may be asked to choose a mail server configuration. Choose "No configuration"

## Rust Server User
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

## Download and run LGSM script
```bash
wget -N --no-check-certificate https://gameservermanagers.com/dl/linuxgsm.sh && chmod +x linuxgsm.sh && bash linuxgsm.sh rustserver
```

## Run the installer and follow the instructions
```bash
./rustserver install
```
When it'll ask you about Server Directory - just hit ENTER

When it'll ask you "Was the install successufl" - hit ENTER

## Editing config files
### Edit common.cfg
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

### Edit server.cfg
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

## Running your Rust Server
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
You can stop your Rust server with:
```bash
./rustserver stop
```
Or restart it:
```bash
./rustserver restart
```

## Try playing at your server
* log in to your Steam account in the Steam app
* run Rust game
* open console by pressing F1
* in the console type (in this example I used 207.154.240.244 IP and 28015 port. You will have different IP. Port should still be 28015 unless you changed it in common.cfg)
```bash
client.connect 207.154.240.244:28015
```
In a couple of minutes server should be present in Rust Community Server listing. You can search for your server by a part of its tytle at http://playrust.io

## Installing Oxide
Navigate to your home directory
```bash
cd ~
```
Stop Rust server if its running
```bash
./rustserver stop
```
Run mods installing utility:
```bash
./rustserver mods-install
```
Once its launched you should see: `Enter an addon/mod to install (or exit to abort):`

Type there:
```bash
rustoxide
```
And wait for it to finish installing. If installation is successful you should see: `Oxide for Rust installed`

Now try starting your server again to see if Oxide had installed correctly
```bash
./rustserver start
```
Check your logs in `/home/rustserveruser/log/server` directory to see if Oxide is loading properly.

If a Rust update has been released, then an Oxide update will soon follow. To update Oxide, you can then run:
```bash
./rustserver mods-update
```

If you want your modded server (if its with Oxide installed it considered modded) to appear in community servers list you should edit oxide.config.json file:
```bash
nano /home/rustserveruser/serverfiles/oxide/oxide.config.json
```
There you should change `"Modded": true` to `"Modded": false`.

WARNING: if you do this to obviously modded server you may get your server blacklisted by FacePunch and not appear in servers list anymore.


## Installing and Updating Oxide Addons
* In order to install Oxide addons just put them into `/home/rustserveruser/serverfiles/oxide/plugins`. They will load automatically.
* If you need to edit their configs, it will be located in `/home/rustserveruser/serverfiles/oxide/config`
* If you updated an addon and wish to reload it without restarting the server you'll need to input it in an RCON tool (like RustAdmin). Once you've got it, run:
```bash
oxide.reload PluginName
```

# Server Management
Updating Rust server
```bash
./rustserver update
```
Validating Rust server
```bash
./rustserver validate
```
Wiping Rust server (change `w1pe` to `wipe` in the command below. Added a typo to avoid accidental wiping)
```bash
./rustserver w1pe
```
Updating Oxide
```bash
./rustserver mods-update
```


## Possible problems and solutions
Server takes about a minute to boot. So if you are getting "Disconnected" messages in the console when you try to log in, you should wait for about a minute or two. If you are still getting "Disconnected" messages this may mean that something is wrong with your installation. Search for logs in `/home/rustserveruser/log/server` folder and try googling any errors that might be there.


# Addons Management
## PlayerReport
[http://oxidemod.org/plugins/playerreport-gui.2635/](http://oxidemod.org/plugins/playerreport-gui.2635/)

Allow default players to report their killers
```bash
oxide.grant group default playerreport.use
```

## Vanish (invisibility addon)
[http://oxidemod.org/plugins/vanish.1420/](http://oxidemod.org/plugins/vanish.1420/)

Allow admins to use /vanish command in chat to become invisible
```bash
oxide.grant group admin vanish.use
```

## AdminRadar
[http://oxidemod.org/plugins/admin-radar.978/](http://oxidemod.org/plugins/admin-radar.978/)

Allows admins to have a radar to help detect cheaters. Any admin can use /radar chat command to show AdminRadar pannel with options

## Night Vision

[http://oxidemod.org/plugins/night-vision.2615/](http://oxidemod.org/plugins/night-vision.2615/)

Allows admins to see everything as if it's day 24/7. To use type in chat `/nightvision`. To activate for admins type in server console:
```bash
oxide.grant group admin nightvision.allowed
```

# Useful Links
* [Most of the info of these instructions was taken from here (guide by UltimateByte)](http://oxidemod.org/threads/setting-up-a-linux-server-with-lgsm.16528/)






