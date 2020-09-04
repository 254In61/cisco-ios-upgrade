#!/bin/bash
echo "Tool is used to upload ios images into devices"
echo "Tool grabs ios ios image file from the usual TFTP Server path, /home/source/uploads and uploads to the cisco device"
echo "Tool takes into consideration possibility of flash or bootflash as a storage directory"
echo "Tool will do a number of checks including 1)flash space 2)Image viability 3)Clean up 1 .bin unused image 4)Md5 checks"
echo "Tool does NOT Reload the device"
echo ""
read -p "CIs hostnames added to the hosts file? y/n:" X
echo ""
if [ "$X" = "y" ]
then
  echo ""
  echo "========Devices to be upgraded========="
  cat hosts
  echo "============================================"
  echo ""
  echo "Perfoming ios upload procedure...."
  iosUpload.yml -k -i hosts
  echo ""
  echo "=============THE END =============="
  echo ""

else
  echo "Please add the CIs hostnames to the hosts file first!!"
  echo ""
  echo "To add devices:"
  echo "Step 1: cat > hosts"
  echo "Step 2: Copy paste your devices in the empty space"
  echo "Step 3: Ctrl + C to close and save"

fi

