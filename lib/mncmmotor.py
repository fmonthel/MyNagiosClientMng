#!/usr/bin/python

import re

class MncmMotor :
    """Class to manage NAGIOS client"""

    def __init__(self, myhostgroups_file, myassetsdir_dir, app_name) :
        
        # Store values
        self.myhostgroups_file = myhostgroups_file
        self.myassetsdir_dir = myassetsdir_dir
        self.app_name = app_name