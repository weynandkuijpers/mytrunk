#!/usr/bin/env python3
# pylint: disable=no-value-for-parameter

# import click
from jumpscale.loader import j
# import stellar_sdk
import os
# from  jumpscale.clients.stellar.exceptions import UnAuthorized

class get_input():
    def __init__(self):
	    self.zdb_number=input('Number of ZDB\'s :')
	    self.zdb_password = input('ZDB password :')
	    self.zdb_size = input('ZDB size :')
	    self.zdb_mode = input('ZDB mode :')

def select_working_pool(my_pools):
    # local temp data storage
    tmp_cus=0
    tmp_sus=0

    # select the largest pool information to pay-as-you-go for the reservation
    for pool in my_pools:
        if (pool.cus >= tmp_cus) or (pool.sus >= tmp_sus):
            if (pool.cus != 0) and (pool.sus != 0):
                pool_id=pool.pool_id
            else:
                print('Cannot use pool_id:', pool_id,' One of the required capacity units is empty')
        tmp_cus=pool.cus
        tmp_sus=pool.sus 
    return(pool_id)

def deploy_zdbs(pool, info, debug_on):
    # local temp data storage
    answer=''
    zos=j.sals.zos.get() 

    # for each node in the pool 
    for node in pool.node_ids:
        zdb_deploy=zos.zdb.create(node_id=node, \
            pool_id=pool.pool_id, \
            password=info.zdb_password, \
            disk_type='HDD', \
            size=info.zdb_size, \
            public='TRUE', \
            mode=info.zdb_mode)
        if debug_on == 1:
            print(zdb_deploy)
            input('Ready?')
        # id=zos.workloads.deploy(zdb_deploy) 
        # result_workload = zos.workloads.get(id) 
        if debug_on == 1:
            print('Workload result:', result_workload)
            input()
            answer=input('Decomission workload?')
            if answer == ('y' or 'Y'): 
                zos.workloads.decomission(id)
                print('Workload ', id, ' decommissioned')

def main():

    # load the SAL to make/break reservation
    zos=j.sals.zos.get() 
	
    # select the pool with the most cus / sus available for deployment
    my_pools=zos.pools.list()
    deploy_pool=select_working_pool(my_pools)
     # get all the data for the selected capacity pool
    my_pool=zos.pools.get(deploy_pool)   
    # 'deploy_pool' now has the capacity pool to deploy ZDB's in.
    # get input for how many and sizing for the ZDB deployment
    zbd_sizing=get_input()
    deploy_zdbs(my_pool, zbd_sizing, 0)

    print('Number: ', zdb_sizing.zdb_number)
    print('Password: ', zdb_sizing.zdb_password)
    print('Size: ', zdb_sizing.zdb_size)
    print('Mode :', zdb_sizing.zdb_mode)

	#pool_id=select_working_pool(my_pools)
	# deploy_zdbs

	# select capacity pool for deployment
    #hello

if __name__ == '__main__':
    main()

# refresh the infromaiton in the pool and print it.
#ipool=zos.pools.get(18714)
#print(pool.active_su)

#zos.workloads.decomission(33312)  

#pool=zos.pools.get(18714)
#pool.active_workload_ids
#[32617, 32621, 32620, 33267, 33269, 33268, 33275, 33278, 33276, 33277, 33281]
