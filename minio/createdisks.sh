#!/bin/bash
dd if=/dev/zero of=myharddisk-1KB.img bs=1000 count=1
dd if=/dev/zero of=myharddisk-10KB.img bs=1000 count=10
dd if=/dev/zero of=myharddisk-100KB.img bs=1000 count=100
dd if=/dev/zero of=myharddisk-1MB.img bs=1000 count=1000
dd if=/dev/zero of=myharddisk-10MB.img bs=1000 count=10000
dd if=/dev/zero of=myharddisk-100MB.img bs=1000 count=100000
dd if=/dev/zero of=myharddisk-1GB.img bs=1000 count=1000000
