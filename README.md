ios_upload ansible playbooks
=============================

These playbooks are developed to upload IOS images onto Cisco Devices.
These playbooks just upload the IOS image and do integrity checks but do not do the following:
1) Change the bootsequence.
2) Reload the devices.

Playbooks 
---------
* main_iosUpload.yml : This is the main playbook that calls on all the other playbooks.
* upload_to_device.yml : Contains tasks that uploads the ios image from Ansible Tower as control machine to the cisco device(s)/hosts.
* file_integrity_checks.yml : Contains tasks that check the integrity of ios image uploaded on the device.

Requirements
------------

* Ansible 2.7.5 and above on the controlling machine.
* The remote device must be running Cisco IOS
* The remote device must support SSH

How to run
----------

* Code is designed to be run from Ansible Tower or CLI of a Linux host.
* You can test on local machine which has reachability to the Artifactory server too with own variables like below;
$ ansible-tower main_iosUpload.yml -u <username> -k -e "@test_vars.yml"

test_vars.tml
---
devices: "192.168.220.214"

in_image: "isr4300-universalk9.03.TESTOS.bin"

...

Variables
---------
The tool expects the following variables:

in_image : Chosen from drop-down on the Ansible-tower or when running from CLI.

devices : List of devices to be processed. Code prepares dynamic inventory from this.

Blueprint schema
------------
Params:

  required: True 

  schema:

    devices:

      type: string

      regex: '[\d]+\.[\d]+\.[\d]+\.[\d]+'

      required: True 

    in_image:

       type: string 

       regex: '[\w\/\.]+' #Matches any word , '/' and '.' .
       
       required: True

Authors
-------

* Allan Maseghe


