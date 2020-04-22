# ciscoIosUpgrade
Ansible Script to do IOS Upgrade for Cisco devices.

Script is split into 2 sections:
1) Pre-implementation stage : Upload IOS 
2) Implementation stage : Upgrade IOS(Reload device).

STEPS Involved:
UPLOAD :
#Step 1: Ontain IOS Facts
#Step 2: Print out device model
#Step 3: Print out current running IOS image
#Step 4: Check new IOS != Old IOS. FAIL if newIOS == oldIOS.
#Step 5: Check validity of the new IOS image by comparing the first 6 characters on the name to the current running image.FAIL if invalid.
#Step 6: Check if device is running on bootflash: or flash:
#Rest of steps are based on the Step 6 output.
#Step 7: Check Space is available in the bootflash/flash.FAIL if memory space < Size of newOS.
#Step 8: Active SCP server
#Step 9: Upload image to the bootflash/flash.
#Step 10: Confirm uploaded newOS file integrity by checking MD5 value.
#Step 11: Set CI boot sequence to newOS.

UPGRADE:
#Step 1: Save configs
#Step 2: Reload device
#Step 3: Confirm successfull upgrade.

