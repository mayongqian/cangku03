from __future__ import print_function

from collections import OrderedDict

import pprint

import os

import sys

import time

def CPUinfo():

    ''' Return the information in /proc/cpuinfo

    as a dictionary in the following format:

    CPU_info['proc0']={...}

    CPU_info['proc1']={...}
    '''

    CPUinfo=OrderedDict()

    procinfo=OrderedDict()



    nprocs = 0

    with open('/proc/cpuinfo') as f:

        for line in f:

            if not line.strip():

                # end of one processor

                CPUinfo['proc%s' % nprocs] = procinfo

                nprocs=nprocs+1
             # Reset

                procinfo=OrderedDict()

            else:

                if len(line.split(':')) == 2:

                    procinfo[line.split(':')[0].strip()] = line.split(':')[1].strip()

                else:

                    procinfo[line.split(':')[0].strip()] = ''



    return CPUinfo



if __name__=='__main__':
    CPUinfo = CPUinfo()

    for processor in CPUinfo.keys():

        print(CPUinfo[processor]['model name'])
def load_stat():

    loadavg = {}

    f = open("/proc/loadavg")

    con = f.read().split()

    f.close()

    loadavg['lavg_1']=con[0]

    loadavg['lavg_5']=con[1]

    loadavg['lavg_15']=con[2]

    loadavg['nr']=con[3]
    loadavg['last_pid']=con[4]

    return loadavg

print("loadavg",load_stat()['lavg_15'])
def meminfo():

    ''' Return the information in /proc/meminfo

    as a dictionary '''

    meminfo=OrderedDict()



    with open('/proc/meminfo') as f:

        for line in f:

            meminfo[line.split(':')[0]] = line.split(':')[1].strip()

    return meminfo



if __name__=='__main__':

    #print(meminfo())



    meminfo = meminfo()

    print('Total memory: {0}'.format(meminfo['MemTotal']))

    print('Free memory: {0}'.format(meminfo['MemFree']))


