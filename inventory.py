#!/usr/bin/env python
#
# inventory.py
#
# Simple tool to list clients and hostgroups from Nagios config files
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
    parser = argparse.ArgumentParser(description='Simple tool to list clients and hostgroups from Nagios config files')
    parser.add_argument('--action', action='store', dest='action', choices=['list-hostgroups','list-clients'], required=True)
    args = parser.parse_args()

    try :
        # MNCM objects instance
        inst_mncm = MncmMotor(Config.get('GLOBAL','application'), Config.get('NAGIOS','myhostgroups'), Config.get('NAGIOS','myassetsdir'))
        # List hostgroups
        if args.action == 'list-hostgroups' :
            logger.info('Request to get the Nagios Hostgroup(s) Ascii Table')
            # Ascii table
            myAsciiTable = [['Hostgroup name','Alias name','Number of client(s)']]
            for key, value in inst_mncm.hostgroups.items() :
                # Build list for output
                tmpdata = list()
                tmpdata.append(key) # Hostgroup
                tmpdata.append(str(value['alias'])) # Alias
                tmpdata.append(str(len(value['members']))) # Number of clients
                # Add tmpdata list to myAsciiTable
                myAsciiTable.append(tmpdata)
            # Create AsciiTable and total
            tmpdata = list()
            tmpdata.append("Total : " + str(len(myAsciiTable) - 1) + " row(s)")
            tmpdata.append("")
            tmpdata.append("")
            myAsciiTable.append(tmpdata)
            myTable = AsciiTable(myAsciiTable)
            myTable.inner_footing_row_border = True
            myTable.justify_columns[2] = 'right'
        # List clients
        if args.action == 'list-clients' :
            logger.info('Request to get the Nagios Client(s) Ascii Table')
            # Ascii table
            myAsciiTable = [['Client name','Address','Type','Nagios Filename']]
            for key, value in inst_mncm.hosts.items() :
                # Build list for output
                tmpdata = list()
                tmpdata.append(value['hostname']) # Hostname
                tmpdata.append(key) # Address
                tmpdata.append(value['hosttype']) # Hosttype
                tmpdata.append(value['filename']) # Filename
                # Add tmpdata list to myAsciiTable
                myAsciiTable.append(tmpdata)
            # Create AsciiTable and total
            tmpdata = list()
            tmpdata.append("Total : " + str(len(myAsciiTable) - 1) + " row(s)")
            tmpdata.append("")
            tmpdata.append("")
            tmpdata.append("")
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