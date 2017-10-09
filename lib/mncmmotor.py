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

        # Testing writable file and dir
        if not os.access(self.myhostgroups_file, os.W_OK) :
            raise RuntimeError('Nagios file "' + self.myhostgroups_file + '" is not writable or not exists :(')
        self.logger.debug('Nagios file "' + self.myhostgroups_file + '" is writable')
        if not os.access(self.myassetsdir_dir, os.W_OK) :
            raise RuntimeError('Nagios dir "' + self.myassetsdir_dir + '" is not writable or not exists :(')
        self.logger.debug('Nagios dir "' + self.myassetsdir_dir + '" is writable')

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
            # Get alias name
            m = re.findall(r"\salias\s(.+)", line)
            if m :
                 alias = m[0]
            # Get members
            m = re.findall(r"\smembers\s(.+)", line)
            if m :
                members = m[0].split(',')
            # End of hostgroup
            if re.match(r"}", line) :
                if members[0] == '*' :
                    self.logger.debug('Ignore hostgroup "' + hostgroup + '" as members = *')
                else :
                    tmpDic[hostgroup] = dict()
                    tmpDic[hostgroup]['members'] = members
                    tmpDic[hostgroup]['alias'] = alias
                    self.logger.debug('Members of "' + hostgroup + '" : ' + str(members))
                # Reset variables
                del members
                del hostgroup
        # Close file and return dictionnary
        myhostgroups.close()
        self.logger.info('End of parsing Nagios file "' + self.myhostgroups_file + '"')
        return tmpDic

    def __hostgroup_exist(self, hostgroup) :
        """Method to check that hostgroup exists"""
        if not type(hostgroup) is str :
            raise RuntimeError('Hostgroup type is not good for variable (str expected)"' + hostgroup + '"')
        if hostgroup in self.hostgroups :
            return True
        else :
            return False
    
    def hostgroups_exist(self, hostgroups) :
        """Method to check that hostgroups exists"""
        if not type(hostgroups) is list :
            raise RuntimeError('Hostgroups type is not good for variable (list expected)"' + hostgroups + '"')
        for hostgroup in hostgroups :
            if not self.__hostgroup_exist(hostgroup) :
                raise RuntimeError('This Nagios configuration doesn\'t know the hostgroup "' + hostgroup + '"')

    def __rewrite_hostgroups_file(self) :
        """Method to rewrite hostgroups file"""
        myhostgroups = open(self.myhostgroups_file, "w+")
        self.logger.info('Rewrite of the Nagios Hostgroup(s) file "' + self.myhostgroups_file + '"')
        # Generic Hostgroup All
        myhostgroups.write("define hostgroup {\n\thostgroup_name all\n\talias All Devices\n\tmembers *\n}")
        # We will now parse each hostgroups to add in the file
        for key, value in self.hostgroups.items() :
            self.logger.debug('Adding hostgroup "' + str(key) + '" in the Nagios hostgroup file : "' + str(value) + '"')
            myhostgroups.write("\ndefine hostgroup {\n\thostgroup_name %s\n\talias %s\n\tmembers %s\n}" % (str(key), str(value['alias']), ','.join(map(str, list(set(value['members']))))))
        # Close file
        self.logger.info('End of rewriting of the Nagios Hostgroup(s) file "' + self.myhostgroups_file + '"')
        myhostgroups.close()

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
                    tmpDic[address]['filename'] = myhost_file
                    self.logger.debug('New host detected : "' + address + '" : ' + str(tmpDic[address]))
                    # Reset variables
                    del hosttype
                    del address
                    del hostname
            # Close file
            myhost.close()
        self.logger.info('End of parsing Nagios directory "' + self.myassetsdir_dir + '"')
        return tmpDic

    def host_exist(self, host) :
        """Method to check that host exists"""
        if not type(host) is str :
            raise RuntimeError('Host type is not good for variable (str expected)"' + host + '"')
        if host in self.hosts :
            return True
        else :
            return False

    def add_host(self, host, hostgroups, hosttype) :
        """Method to add client into the Nagios configuration"""
        if not type(host) is str :
            raise RuntimeError('Host type is not good for variable (str expected)"' + host + '"')
        if not type(hostgroups) is list :
            raise RuntimeError('Hostgroups type is not good for variable (list expected)"' + hostgroups + '"')
        if not type(hosttype) is str :
            raise RuntimeError('Hosttype type is not good for variable (str expected)"' + hosttype + '"')
        # Creation file into assetdir
        myhost_file = os.path.join(self.myassetsdir_dir + '/' + host + '.cfg')
        self.logger.info('Creation of the file "' + myhost_file + '"')
        myhost = open(myhost_file, "w+")
        myhost.write("define host {\n\tuse %s\n\thost_name %s\n\taddress %s\n}" % (hosttype, host, host))
        myhost.close()
        # Adding the host into hostgroups
        for hostgroup in hostgroups :
            self.hostgroups[hostgroup]['members'].append(host)
            self.logger.debug('Adding host "' + host + '" into the hostgroup "' + hostgroup + '"')
        # Rewrite of the Nagios Hostgroup file
        self.__rewrite_hostgroups_file()