#
# Copyright 2014 Microsoft Corporation
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Requires Python 2.4+ and Openssl 1.0+
#

import os
import re
import pwd
import shutil
import socket
import array
import struct
import fcntl
import time
import azurelinuxagent.logger as logger
import azurelinuxagent.utils.fileutil as fileutil
import azurelinuxagent.utils.shellutil as shellutil
import azurelinuxagent.utils.textutil as textutil
from azurelinuxagent.distro.debian.osutil import DebianOSUtil

class UbuntuOSUtil(DebianOSUtil):
    def __init__(self):
        super(UbuntuOSUtil, self).__init__()

    def StartNetwork(self):
        return shellutil.Run("service networking start", chk_err=False)
   
class Ubuntu1204OSUtil(UbuntuOSUtil):
    def __init__(self):
        super(Ubuntu1204OSUtil, self).__init__()

    #Override
    def GetDhcpProcessId(self):
        ret= shellutil.RunGetOutput("pidof dhclient3")
        return ret[1] if ret[0] == 0 else None

