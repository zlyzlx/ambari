"""
Licensed to the Apache Software Foundation (ASF) under one
or more contributor license agreements.  See the NOTICE file
distributed with this work for additional information
regarding copyright ownership.  The ASF licenses this file
to you under the Apache License, Version 2.0 (the
"License"); you may not use this file except in compliance
with the License.  You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

"""

from resource_management import *

config = Script.get_config()

oozie_user = config['configurations']['global']['oozie_user']
falcon_user = config['configurations']['global']['falcon_user']
smoke_user =  config['configurations']['global']['smokeuser']

java_home = config['hostLevelParams']['java_home']
falcon_home = '/usr/lib/falcon'
falcon_conf_dir = '/etc/falcon/conf'
falcon_local_dir = config['configurations']['global']['falcon_local_dir']
falcon_log_dir = '/var/log/falcon'
falcon_data_dir = format('{falcon_local_dir}/activemq')
store_uri = config['configurations']['global']['falcon_store_uri']
falcon_host = config['clusterHostInfo']['falcon_server_hosts'][0]
falcon_port = config['configurations']['global']['falcon_port']

#for create_hdfs_directory
security_enabled = (config['configurations']['core-site']['hadoop.security.authentication'] == 'kerberos')
hostname = config["hostname"]
hadoop_conf_dir = "/etc/hadoop/conf"
hdfs_user_keytab = config['configurations']['global']['hdfs_user_keytab']
hdfs_user = config['configurations']['global']['hdfs_user']
kinit_path_local = functions.get_kinit_path([default("kinit_path_local",None), "/usr/bin", "/usr/kerberos/bin", "/usr/sbin"])
import functools
#create partial functions with common arguments for every HdfsDirectory call
#to create hdfs directory we need to call params.HdfsDirectory in code
HdfsDirectory = functools.partial(
  HdfsDirectory,
  conf_dir=hadoop_conf_dir,
  hdfs_user=hdfs_user,
  security_enabled = security_enabled,
  keytab = hdfs_user_keytab,
  kinit_path_local = kinit_path_local
)
