# Simple  Farmers network setup.

So you have become a farmer. And you have bought some shiny new nodes to host the Threefold Grid and provide for services in that grid.

Grid means network. The network is the computer. 

This document surmises you will connect several nodes on a network, separate from other networks in your location, solely for the purpose to add nodes to the grid in a more professional setup, where multiple nodes live on the same setup

## Necessities

What you'll need.

  - a link to the Internet with appropriate bandwith for the services you want to provide.
  - a router that connects your internal network with the Internet Uplink.  This can be a simple Set-Top box provided by the network provider or a more professional dedicated router. 
  - one or more switches in function of the number of nodes you need to connect
  - medim knowledge about how to configure your switch and router with regards to:
    - managing public IP addresses on the public router
    - managing the switch capabilities of the router or managing a seperate switch
    - managing the DHCP capabilities of the router or mantain a seprate DHCP server on  your home or corporate network.


## What it's going to look like

### __physical layout__

```
+                                
|  Internet link           
|          +-------------------+
|          |  Router           +
+----------+  NAT FW           |
           |                   +
+-------+  +-+-+---------------+ 
|DHCP   |    |              
|server |    |
|       |    |                     
+---+---+  +-+-+------------+    
    |      | Switch         |  
    +------+  vlan          |
           |                | 
           +-+--------------+
             |           |         
             |           |           
      NIC 1  |           |  (NIC 2 optional) 
           +-+-----------+-----+     
           | NODES             +-+   
           |                   | +-+  
           |                   | | +-+ 
           +-------------------+ | | |  
            +--------------------+ | +
             +---------------------+ | 
              +----------------------+

```
The setup here is drawn without Highly available routers or multi-switch link aggregation, thus fairly simple.    

There can be an optional Internet link for when a farmer has possibility to have nultiple uplinks to create upstream network redundacy. This will not be discussed here as we suppose a farmer has the necessary knowledge in house to properly configure BGP and routing in case of such a setup.

### __logical layout__

In order for nodes to properly boot, they need to download and start 0-OS: 
  - with a bios configured to boot from an USB stick
  - with a bios configured to boot from the network

Either way, a node needs to obtain an IP address and access the Internet to be able to downlaod 0-OS and boot it.

To give a node an IP address you'll need to setup a DHCP server that provides for an IP address to one of the NICs of the nodes. At freefarm, we configure the DHCP server to provide specific IP addresses to nodes in function of their MAC address on the management as wel as on the OOB network, so that we can be sure which physical node receives which IP address.
That makes it easier to physically locate them. A small drawback is that we have to recense all the mac addresses and confiure the DHCP server prior to booting them, but as we need to access all bios anyway, we can do that while racking and configuring the bios.


# Network Functionality of 0-OS

## boot steps

After iPXE or USB installed and booted the kernel, `zinit` as PID 1, starts `internet`.
That process is a single_run application that tries to get internet going in a node.
These are the steps:
  1. enable all interfaces that are found byo 0-OS.
  1. on all these interfaces, start a DHCP client, and enable SLAAC for IPv6.
  Wait for interfaces to settle, and make a list of received IPv[46] addresses
  1. The interface that received an RFC1918 address AND that could reach the Internet through it's received default gateway becomes the master of the zos bridge
  1. task is done, register the DHCP client on the zos bridge in zinit, so it gets restarted if neceassary, and disable IPv6 on the slave interface that got connected to the zos bridge.
  1. exit

## start of network

Once 0-OS has established a management NIC and set it to be slave of the zos bridge, 0-OS basically searches again for a NIC (except `zos`) that has a link and recieves an IPv6 global unicast address.
That NIC becomes a slave of a `br-pub` bridge. 

If __NO__ NIC has been found that has received an IPv6 address in a timely manner, the bridges `zos` and `br-pub` get connected together so that the management segment becomes the network to forward packets.

0-OS works IPv6 first.
That means that either way, to get the most out of the grid, getting IPv6 in your network is the best thing to do.
But there are situations where there is no IPv6 (or at least, no IPv6 with a gatway), where we the start an overlay network that can still provide for IPv6, based on Yggdrasil, so that services on the grid stay reachable. 

So it can be that:
  - The node has only 1 (one) NIC connected
    - zos has an RFC1918 address and no IPv6 global unicast.(HIDDEN NODE)  
      Then the zos and br-pub bridge get connected, and the sole way to reach services on the node (lik 0-DB) is through the yggdrasil overlay network
    - zos has received an RFC1918 address, AND an IPv6 global unicast.  
    While the yggdrasil overlay network is still installed so the hidden nodes can reach the services of this node, full IPv6 services over the global unicast IPv6 network is enabled, except when a node lives behind a firewalled IPv6 network.  
    If firewalled, 0-OS detects that and flags the node as hidden in the explorer
  - The node has 2 NICs connected.  
  It needs to be said that if 2 NICs are connected, 0-OS surmises that one of the NIcs __will__ receive a global unicast IPv6 address, and if it doesn't, will flag it as a hidden node.

## public_config