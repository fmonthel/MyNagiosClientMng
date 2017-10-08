#!/usr/bin/env python
#
# motor.py
#
# Simple tool to manage client into Nagios config files
#
# Author: Florent MONTHEL (fmonthel@flox-arts.net)
#

import os
import re
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
    logging.basicConfig(level=logging.DEBUG)
    logger = logging.getLogger(Config.get('GLOBAL','application'))
    handler = logging.FileHandler(os.path.join(os.path.dirname(__file__), 'log/'+Config.get('GLOBAL','application')+'.log'))
    handler.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    # Options
    parser = argparse.ArgumentParser(description='Simple tool to manage client into Nagios config files')
    parser.add_argument('--action', action='store', dest='action', choices=['list-hostgroups'], required=True)
    args = parser.parse_args()

    # MNCM objects instance
    try :
        inst_mncm = MncmMotor(Config.get('GLOBAL','application'), Config.get('NAGIOS','myhostgroups'), Config.get('NAGIOS','myassetsdir'))
    except Exception as e :
        logger.error('RunTimeError during instance creation : %s', str(e))
        raise RuntimeError('Exception during instance creation : ' + str(e))

if __name__ == "__main__" :
    main()