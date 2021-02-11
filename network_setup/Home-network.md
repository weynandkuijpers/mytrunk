# The "Home farmer" network setup.

So you have become a farmer. And you have bought a shiny new noded to host the Threefold Grid and provide for services in that grid. Cool, let's get you started

Grid means network. The network is the computer. Your node is becoming part of a global grid of computers where people can rent capacity and deploy applications withouh using one of the market leading monopolies, but by (potentially) using your node in your home.

This document will handle the network setup/requirements for a home deployment.  There is more to it that just setting up the network and for that re refer you to the 

## Necessities

What you'll need.

  - a link to the Internet with appropriate bandwith for the services you want to provide. Typically this will come from a telecom operator in you reagion and it will be in the form of a consumer access product 
  - a set-top box (router) that connects your home/business with a Internet Uplink to the internet.
  - one or more switches in function of the number of nodes you need to connect
  - some knowledge about how to configure your switch and router

## What it's going to look like

### __physical layout__

```
+                                   
|           Set-Top box                            
|          +-------------------+          
|          |  Router           |
+----------+  NAT FW           |
           |  Switch           |
           |  DHCP Server      |
           +-+-----------------+   
             |         
             |  Nertwork connection 1 (On Set-Top box and Nodes)       
             |         
           +-+-----------------+ 
           | NODES             +-+  
           |                   | +-+
           |                   | | +-+ 
           +-------------------+ | | |
            +--------------------+ | +
             +---------------------+ | 
              +----------------------+

```
The setup here is fairly simple.   All functionality required exists in the set-top box provided by the network provider (DSL, Fibre, Wireless).  The only thing that is required is to connect the ThreeFold node to one of the available ports on the set-top box with a network cable and you shoul be good to go.  The ThreeFold device will act as one of you household (office) devices and make se of the available bandwidth to the internet provider by the set-top box.