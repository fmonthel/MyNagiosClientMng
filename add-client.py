#!/usr/bin/env python
#
# add-client.py
#
# Simple tool to add client to Nagios config files
#
# Author: Florent MONTHEL (fmonthel@flox-arts.net)
#

import os
import ConfigParser
import argparse
import logging
import datetime
from terminaltables import AsciiTable
from lib.mncmmotor import MncmMotor

def main() :

    # Parameters
    time_start = datetime.datetime.now()
    file_config = os.path.join(os.path.dirname(__file__), 'conf/config.ini')
    Config = ConfigParser.ConfigParser()
    Config.read(file_config)

    # Logging setup
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(Config.get('GLOBAL','application'))
    handler = logging.FileHandler(os.path.join(os.path.dirname(__file__), 'log/'+Config.get('GLOBAL','application')+'.log'))
    handler.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    # Options
    parser = argparse.ArgumentParser(description='Simple tool to add client into Nagios config files')
    parser.add_argument('--address', action='store', dest='address', help='FQDN of the asset', required=True)
    parser.add_argument('--hosttype', action='store', dest='hosttype', choices=['linux-server','generic-switch'], required=True)
    parser.add_argument('--hostgroups', action='store', dest='hostgroups', help='List of hostgroup(s) comma separated', required=True)    
    args = parser.parse_args()

    try :
        # MNCM objects instance
        inst_mncm = MncmMotor(Config.get('GLOBAL','application'), Config.get('NAGIOS','myhostgroups'), Config.get('NAGIOS','myassetsdir'))
        # Check if the client doesn't exist already
        logger.info('Check if client "' + str(args.address) + '"+ is not already part of this configuration')
        if inst_mncm.host_exist(str(args.address)) :
            raise RuntimeError('The client "' + str(args.address) + '" is already part of this configuration')
        # Check if the hostgroups exist
        logger.info('Check if hostgroup(s) "' + str(args.hostgroups.split(',')) + '" is part of this configuration')
        inst_mncm.hostgroups_exist(str(args.hostgroups).split(','))
        # We can add the client :)
        logger.info('Adding client "' + str(args.address) + '" in the Nagios configuration with hostgroup(s) "' + str(args.hostgroups.split(',')) + '"')
        inst_mncm.add_host(str(args.address),str(args.hostgroups).split(','),str(args.hosttype))
        # Ascii table
        myAsciiTable = [['Client address','Type','Hostgroup(s)']]
        tmpdata = list()
        tmpdata.append(str(args.address)) # Address
        tmpdata.append(str(args.hosttype)) # Hosttype
        tmpdata.append(str(args.hostgroups)) # Hostgroup(s)
        # Add tmpdata list to myAsciiTable
        myAsciiTable.append(tmpdata)
        myTable = AsciiTable(myAsciiTable)
        myTable.inner_footing_row_border = True
        # End script
        time_stop = datetime.datetime.now()
        time_delta = time_stop - time_start
        # Output data
        print "######### DATE : %s - APP : %s #########" % (time_start.strftime("%Y-%m-%d"),Config.get('GLOBAL','application'))
        print "- Start time : %s" % (time_start.strftime("%Y-%m-%d %H:%M:%S"))
        print "- Finish time : %s" % (time_stop.strftime("%Y-%m-%d %H:%M:%S"))
        print "- Delta time : %d second(s)" % (time_delta.total_seconds())
        print myTable.table

    except Exception as e :
        logger.error('RunTimeError during instance creation : %s', str(e))

if __name__ == "__main__" :
    main()