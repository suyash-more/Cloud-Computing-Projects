
## Installation / Download and Reference Material

 - [Oracle's Virtual Box](https://www.virtualbox.org/wiki/Downloads)
 - Ubuntu 64 VMDK Image [Option 1](https://drive.google.com/drive/u/0/folders/1me_nJJh0fvdDOXX3ew2jzGQpoP7f_iFt)  or [Option 2](https://app.vagrantup.com/bento/boxes/ubuntu-18.04)
 - [SCP Article](https://linuxize.com/post/how-to-use-scp-command-to-securely-transfer-files/)

Follow [this video](https://youtu.be/0MaS0nZCTZc) for live implementation of this problem statement.


### Steps :
1. Download and install Oracle's Virtual Box. (Reboot needed after installation)

2. Download Ubuntu VMDK Image.

3. Launch Virtualbox and create a new VM.

4. Click on new and mention the Name and the machine folder along with the Type and Version of the Machine to be created.

5. Assign memory size for our VM (1024 MB sufficient for now).

6. Select the option **Use an existing virtual hard disk file** and locate the donwloaded VMDK image below and create VM.

7. Now we have to create a NAT Network so go to **File -> Preferences -> Network -> Add a New NAT Network (Click on **+**)**

8. Right click and edit the Network name and CIDR if needed.
Example : 
```
Name - My VMbox Network
CIDR - 172.168.2.0/24 and save the changes.
```

9. Repeat the process of launching the VM for 2 instances.

10. Now go to the setting, go to the network setting and change the adapter to NAT Network and  and select the NAT Network you made ( in our case : **My VMbox Network** ) and click ok.

11. Launch the VM now.

12. Install the net-tools to know the IP's of the instance.
```sh
$ sudo apt install net-tools
$ sudo apt update
```

13. To know the IP address
```sh
$ ifconfig
```
Now the IP will be in the range of __172.168.2.*__ 
```
 * - any number in the range of 1 to 254 (total 256 addresses)
```

14. Now create a file and write something into it.
```sh
$ touch tranfer.txt
$ nano transfer.txt
-> hey, How are you?
ctrl + X and save
```

```
Some Commands for Linux Based Distros:

ls - list all the files and directories
cat - show the content inside a file
scp - it will help us to copy files from one vm to other
cd - change directory
mkdir - make a new directory
touch - it makes a new file 
nano - nano is a editor inside linux os

```
15. If your file is on the VM with IP **172.168.2.4** and the second VM's IP is **172.168.2.5**.

16. Tranfer the file using **SCP**
```sh
$ scp tranfer.txt vagrant@172.168.2.5:/home/vagrant
```
Put in the password of the 2nd VM and done.

17. Check for the file in the Second VM under the **/home/vagrant** directory.

18. Done..!!!!
 