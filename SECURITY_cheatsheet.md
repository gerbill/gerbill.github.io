# SECURITY CHEAT SHEET

## Passwordless SSH login

#### STEP ONE: Generate an RSA key using ssh-keygen on your local machine
Unless you've already created one!
```bash
ssh-keygen -t rsa
```
This creates a public/private keypair of the type (-t) rsa.
```bash
Generating a public/private rsa key pair.
Enter the file in which you wish to save they key (i.e., /home/username/.ssh/id_rsa).
```
Once the keypair is created, you are prompted to enter the following items. 
Click Enter on your keyboard to continue.
```bash
Enter a passphrase (leave empty for no passphrase).
```
Click Enter on your keyboard to continue.
```bash
Enter same passphrase again:
```
Click Enter on your keyboard to continue.
When finished, click Enter on your keyboard.
The following message appears:
```bash
Your identification has been saved in /home/username/.ssh/id_rsa
Your public key has been saved in /home/username/.ssh/id_sra.pub

The key fingerprint is:
ar:bc:d3:9e:g3:1f:63:6f:6b:32:2e:97:ee:42:e1:be username@server.dreamhost.com

The key’s randomart image is:

+--[ RSA 2048]----+
| ..+**B.o++o     |
|  . o+==o. o     |
|    . .oo.=      |
|      . +E+ .    |
|        S .      |
|                 |
|                 |
|                 |
|                 |
+-----------------+
```

#### STEP TWO: Copying the public key to Linux VPS or server

Copy the public key on your local computer to Linux server by running the following command on your Linux or Mac machine.
```bash
ssh-copy-id -i ~/.ssh/id_rsa.pub username@51.51.51.51
```
You will be asked to enter password for this username on a remote Linux server. After that you will be asked to enter your RSA key password.
