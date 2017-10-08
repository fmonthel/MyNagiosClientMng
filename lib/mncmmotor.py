#!/usr/bin/python

import re
import os
import logging

class MncmMotor :
    """Class to manage NAGIOS client"""

    def __init__(self, app_name, myhostgroups_file, myassetsdir_dir) :

        # Class name
        self.class_name = self.__get_class_name()
        # Logger
        self.logger = logging.getLogger(app_name+'.'+self.class_name)
        self.logger.info('Creating an instance of %s', self.class_name)
        
        # Store values
        if not isinstance(app_name, str) or not isinstance(myhostgroups_file, str) or not isinstance(myassetsdir_dir, str) :
            raise TypeError('Invalid type : app_name, myhostgroups_file, myassetsdir_dir must be a string')
        self.myhostgroups_file = myhostgroups_file
        self.myassetsdir_dir = myassetsdir_dir
        self.app_name = app_name
        
        # Testing readable file and dir
        if not os.access(self.myhostgroups_file, os.R_OK) :
            raise RuntimeError('Nagios file "' + self.myhostgroups_file + '" is not readable or not exists :(')
        if not os.access(self.myassetsdir_dir, os.R_OK) :
            raise RuntimeError('Nagios dir "' + self.myassetsdir_dir + '" is not readable or not exists :(')

    def __get_class_name(self) :
        """Method to have instance name of class (str)"""

        return self.__class__.__name__