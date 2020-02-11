## Standalone testnet setup of ThreeFold technology

### Get a bootable zero-OSV2.0 image 

1. Download a zeroOSV2.0 image
   1. The images can be found here: https://dev.bootstrap.grid.tf/.  There is a choice of 3 boot modes for ZeroOSV2.0: production, development and test. This is set by a boot option passed onto the kernel during boot.  
[](./images/choose_release.png)
   2. One input box is available to enter the farmerID.  The farmerID is different than what was used for version 1.0.  The farmerID is a number in zeroOSV2.0.  There is no public facility to find/trace the farmerID today so as we are not farming for tokens any number works
[](./images/farmer_id.png)  
   3. Choose the wanted image type - there are 4 image types available. 
[](./images/choose_image_type.png) 
   2. Transport the downloaded file to a USB stick.  Use the tool that is supported by your operating system.
   3. Boot the server from the USB stick

This should get you a booted ZeroOSV2.0 which has a number of development options enabled (by default, this will change going forward).

It also is configured to look at a certain blockchain database (bcdb) to see what workloads are ready for this node.  Next step is that we alter this and to look and  compile a local (mock) blockchain DB so that we can start and stop containers.

## Get the toolset to create a local standalone testnet
To build a local testnet setup we need to to get the zos repository from github.  This repository can be found here: https://github.com/threefoldtech/zos. To download this repository you need to have a working version of git installed.  This has to be done on a linux machine as some of the tools require libraries that are available for linux only.

```git clone https://github.com/threefoldtech/zos.git```  

[](./images/zos_repo_clone.png)
The zos repository contains all of the code for zeroOSV2.0, we only need to have a look at the “tools” directory

To compile the tools, the development environment and golang development suite has to be installed.  On ubuntu this can be done by typing the command

```sudo apt install golang```

[](./images/install_golang.png)

Make also sure the make tool is installed:
```sudo apt install make```

Now type ```make``` in the tools directory

[](./images/tools_compile.png) 
 
All tools required to create a private testnet environment are now compiled and are available.