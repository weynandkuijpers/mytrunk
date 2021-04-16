#!/usr/bin/env python3
# pylint: disable=no-value-for-parameter

import click
from jumpscale.loader import j
import stellar_sdk
import os
from  jumpscale.clients.stellar.exceptions import UnAuthorized

# load the SAL to make/break reservation
zos=j.sals.zos.get() 

my_pools=zos.pools.list()

tmp_cus=0
tmp_sus=0

# select the largest pool information to pay-as-you-go for the reservation
for pool in my_pools:
    if pool.cus >= tmp_cus or pool.sus >= tmp_sus:
        if pool.cus != 0 and pool.sus != 0:
            pool_id=pool.pool_id
        else:
            print('Cannot use pool_id:', pool_id,' One of the required capacity units is empty')
    tmp_cus=pool.cus
    tmp_sus=pool.sus 

print('Selected pool to deploy ZDB\'s:', pool_id)
my_pool=zos.pools.get(pool_id)

# check my identity (so see if I own the pool)
# j.core.identity.me

zdb_nodes=[]

# list the available nodes in this particular pool
for node in my_pool.node_ids:
    print(node)    
#    zdb_node=pool.node_ids[0]

#zdb_deployed=zos.zdb.create(node_id='FbMBh3gGX5WLkcVgvxtTZ32ZiQwoAUUfcDvdMp8fLP8H', pool_id=pool.pool_id, password='supersecret', disk_type='HDD', size=256, public='TRUE', mode='seq')

#id=zos.workloads.deploy(zdb_deployed) 
#result_workload = zos.workloads.get(id) 
#print(result_workload)                                                                                                                    

'''ZdbNamespace(
  id=33312,
  node_id='FbMBh3gGX5WLkcVgvxtTZ32ZiQwoAUUfcDvdMp8fLP8H',
  size=256,
  mode=<ZDBMode.Seq: 0>,
  password='1c22c0544ec9d35f0262e646621f4c6aafc83696378997ba6394e6bff48eb957e2822e61f7a6a29335ac1d4679a3cf09b4bef5',
  disk_type=<DiskType.HDD: 0>,
  public=False,
  stats_aggregator=[],
  info=ReservationInfo(
  workload_id=1,
  node_id='FbMBh3gGX5WLkcVgvxtTZ32ZiQwoAUUfcDvdMp8fLP8H',
  pool_id=18714,
  description='',
  reference='',
  customer_tid=2077,
  customer_signature='7976fe3d219e346f325ad2d4b55c11ec7057cc2194eee5010c42a09ab057813ce16b3480a4a755b766146a432431d4afce42d19b2126f41bd08c8b0a777e6204',
  next_action=<NextAction.DEPLOY: 3>,
  signatures_provision=[],
  signing_request_provision=SigningRequest(
  signers=[],
  quorum_min=0
),
  signing_request_delete=SigningRequest(
  signers=[2077],
  quorum_min=1
),
  signatures_farmer=[],
  signatures_delete=[],
  epoch=datetime.datetime(2021, 4, 16, 5, 44, 15, tzinfo=tzutc()),
  metadata='',
  result=ReservationResult(
  category=<Category.Zdb: 0>,
  workload_id='33312-1',
  data_json='{"Namespace": "33312-1", "IPs": ["2a10:b600:1:0:b411:e3ff:fe56:9f1f", "300:2cb9:24f1:6677:b7b9:59c2:1362:730"], "Port": 9900}',
  signature=b'76e9ffce785b72eba787c10fe17adb5d880e06231ba3fc773625a25ba72f8eef4257d27f51987c3525dfe5c1a5adcdd4c2ba4289c7f7b78b4c5e818d5bda5003',
  state=<State.Ok: 1>,
  message='',
  epoch=datetime.datetime(2021, 4, 16, 5, 44, 18, tzinfo=tzutc())
),
  workload_type=<WorkloadType.Zdb: 0>
)
)
'''

# refresh the infromaiton in the pool and print it.
#ipool=zos.pools.get(18714)
#print(pool.active_su)

#zos.workloads.decomission(33312)  

#pool=zos.pools.get(18714)
#pool.active_workload_ids
#[32617, 32621, 32620, 33267, 33269, 33268, 33275, 33278, 33276, 33277, 33281]
