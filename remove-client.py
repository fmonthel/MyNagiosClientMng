#!/usr/bin/env python
#
# add-client.py
#
# Simple tool to remove client to Nagios config files
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
    parser = argparse.ArgumentParser(description='Simple tool to remove client from Nagios config files')
    parser.add_argument('--address', action='store', dest='address', help='FQDN of the asset', required=True)
    args = parser.parse_args()

    try :
        # MNCM objects instance
        inst_mncm = MncmMotor(Config.get('GLOBAL','application'), Config.get('NAGIOS','myhostgroups'), Config.get('NAGIOS','myassetsdir'))
        # Check if the client exist already
        logger.info('Check if client "' + str(args.address) + '" is part of this configuration')
        if not inst_mncm.host_exist(str(args.address)) :
            raise RuntimeError('The client "' + str(args.address) + '" is not part of this configuration')
        # We can remove the client :)
        logger.info('Removing client "' + str(args.address) + '" from the Nagios configuration')
        inst_mncm.remove_host(str(args.address))
        # Ascii table
        myAsciiTable = [['Client address','Action']]
        tmpdata = list()
        tmpdata.append(str(args.address)) # Address
        tmpdata.append('Removed') # Hosttype
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