#!/usr/bin/python

import re
import os
import glob
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
        # Get hosts
        self.hosts = self.__get_hosts()

    def __get_class_name(self) :
        """Method to have instance name of class (str)"""
        return self.__class__.__name__

    def __get_hostgroups(self) :
        """Method to get Nagios hostgroups and return dic"""
        # Dic
        tmpDic = dict()
        # Open file
        myhostgroups = open(self.myhostgroups_file)
        self.logger.info('Starting parsing Nagios file "' + self.myhostgroups_file + '"')
        for line in myhostgroups :
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
        myhostgroups.close()
        self.logger.info('End of parsing Nagios file "' + self.myhostgroups_file + '"')
        return tmpDic

    def __get_hosts(self) :
        """Method to get Nagios hosts and return dic"""
        # Dic
        tmpDic = dict()
        # Parsing directory
        self.logger.info('Starting parsing Nagios directory "' + self.myassetsdir_dir + '"')
        for myhost_file in glob.glob(self.myassetsdir_dir + "/*.cfg") :
            # Open file
            myhost = open(myhost_file)
            self.logger.debug('Starting parsing Nagios host file "' + myhost_file + '"')
            for line in myhost :
                # Get hostname
                m = re.findall(r"\shost_name\s(.+)", line)
                if m :
                     hostname = m[0]
                # Get address
                m = re.findall(r"\saddress\s(.+)", line)
                if m :
                     address = m[0]
                # Get hosttype
                m = re.findall(r"\suse\s(.+)", line)
                if m :
                     hosttype = m[0]
                # End of host
                if re.match(r"}", line) and address and hosttype and hostname :
                    tmpDic[address] = dict()
                    tmpDic[address]['hosttype'] = hosttype
                    tmpDic[address]['hostname'] = hostname
                    self.logger.debug('New host detected : "' + address + '" : ' + str(tmpDic[address]))
                    # Reset variables
                    del hosttype
                    del address
                    del hostname
            # Close file
            myhost.close()
        self.logger.info('End of parsing Nagios directory "' + self.myassetsdir_dir + '"')
        return tmpDic        