#!/bin/bash

apt update
apt upgrade -y
apt install git -y
apt install bmon -y
mkdir $HOME/opt
cd $HOME/opt
git clone https://github.com/weynandkuijpers/mytrunk.git
cd mytrunk/minio
wget https://dl.min.io/client/mc/release/linux-amd64/mc
chmod +x mc
