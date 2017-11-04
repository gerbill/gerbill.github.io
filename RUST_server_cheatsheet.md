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
adduser rustserver
```
```bash
passwd mystrongpassword
```
Login with this newly created user
```bash
su rustserver
```
#### Download and run LGSM script
```bash
wget -N --no-check-certificate https://gameservermanagers.com/dl/linuxgsm.sh && chmod +x linuxgsm.sh && bash linuxgsm.sh rustserver
```

#### Run the installer and follow the instructions
```bash
./rustserver install
```
















