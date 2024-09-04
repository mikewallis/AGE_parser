#!/bin/env python
import sys
import pandas as pd

if len(sys.argv) > 1:
    filename = sys.argv[1]
else:
    print("Usage: "+sys.argv[0] +" <path_to_logfile>")
    exit()

# this is just defining the cols and dropping the ones we don't use
# remember, latin-1 encoding! otherwise 'submit_cmd' will fail

df = pd.read_csv(filename,sep=':',names=[
   'qname',
   'hostname',
   'grp',
   'owner',
   'job_name',
   'job_number',
   'account',
   'priority',
   'submission_time',
   'start_time',
   'end_time',
   'failed',
   'exit_status',
   'ru_wallclock',
   'ru_utime',
   'ru_stime',
   'ru_maxrss',
   'ru_ixrss',
   'ru_ismrss',
   'ru_idrss',
   'ru_isrss',
   'ru_minflt',
   'ru_majflt',
   'ru_nswap',
   'ru_inblock',
   'ru_oublock',
   'ru_msgsnd',
   'ru_msgrcv',
   'ru_nsignals',
   'ru_nvcsw',
   'ru_nivcsw',
   'project',
   'department',
   'granted_pe',
   'slots',
   'task_number',
   'cpu',
   'mem',
   'io',
   'category',
   'iow',
   'pe_taskid',
   'maxvmem',
   'arid',
   'ar_submission_time',
   'job_class',
   'qdel_info',
   'maxrss',
   'maxpss',
   'submit_host',
   'cwd',
   'submit_cmd',
   'wallclock',
   'ioops',
   'bound_cores'
  ],usecols=[
   'qname',
   'hostname',
   'grp',
   'owner',
   'job_name',
   'job_number',
   'account',
   'priority',
   'submission_time',
   'start_time',
   'end_time',
   'failed',
   'exit_status',
   'ru_wallclock',
   'project',
   'department',
   'granted_pe',
   'slots',
   'task_number',
   'cpu',
   'mem',
   'io',
   'category',
   'iow',
   'pe_taskid',
   'maxvmem',
   'arid',
   'ar_submission_time',
   'job_class',
   'qdel_info',
   'maxrss',
   'maxpss',
   'submit_host',
   'cwd',
   'submit_cmd',
   'wallclock',
   'ioops'
  ],encoding='latin_1',skip_blank_lines=True,error_bad_lines=False,warn_bad_lines=True,engine='python')

# do stuff here
pd.set_option('display.max_rows',None)
pd.set_option('display.max_columns',None)
pd.set_option('display.float_format', lambda x: '%.3f' % x)
#sys.stdout = open("output_"+filename,"w")
csv_data=df.groupby(['owner','qname','project','slots'])['cpu'].agg(['sum','count','mean','median','std','min','max']).to_csv("output_"+filename+".csv")
#sys.stdout.close()
