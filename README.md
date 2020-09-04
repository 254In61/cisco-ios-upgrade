Ansible Script to do IOS Upgrade for Cisco devices.

-Script will :

1)Confirm file exists in Linux FTP server and check size plus MD5 value.

2) Collect ios facts

3) Check if device uses flash or bootflash

4) Confirm device does not use the new IOS

5) Confirm new IOS image is valid for the device[Compare first 8 characters of file name]

6) Confirm enough space for new ios image upload

7) Upload IOS Image

8) Do MD5 checks.

9) Change boot sequence.

10) Save running configs

**DOES NOT RELOAD THE DEVICE**


