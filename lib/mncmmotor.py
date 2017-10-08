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
        self.logger.debug('Nagios file "' + self.myhostgroups_file + '" is readable')
        if not os.access(self.myassetsdir_dir, os.R_OK) :
            raise RuntimeError('Nagios dir "' + self.myassetsdir_dir + '" is not readable or not exists :(')
        self.logger.debug('Nagios dir "' + self.myassetsdir_dir + '" is readable')

        # Get hostgroups
        self.hostgroups = self.__get_hostgroups()

    def __get_class_name(self) :
        """Method to have instance name of class (str)"""

        return self.__class__.__name__
    
    
    def __get_hostgroups(self) :
        """Method to get Nagios hostgroups and return dic"""
        
        # Dic
        tmpDic = dict()
        # Open file
        myhostgroups_file = open(self.myhostgroups_file)
        self.logger.info('Starting parsing Nagios file "' + self.myhostgroups_file)
        for line in myhostgroups_file :
            # Get hostgroup name
            m = re.findall(r"\shostgroup_name\s(.+)", line)
            if m :
                 hostgroup = m[0]
            # Get members
            m = re.findall(r"\smembers\s(.+)", line)
            if m :
                members = m[0].split(',')
            # End of hostgroup
            if re.match(r"}", line) :
                if members[0] == '*' :
                    self.logger.debug('Ignore hostgroup "' + hostgroup + '" as members = *')
                else :
                    tmpDic[hostgroup] = members
                    self.logger.debug('Members of "' + hostgroup + '" : ' + str(members))
                # Reset variables
                del members
                del hostgroup
        # Close file and return dictionnary
        myhostgroups_file.close()  
        self.logger.info('End of parsing Nagios file "' + self.myhostgroups_file)
        return tmpDic