# MyNagiosClientMng

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/296734d54ebc4a608328c887225114f9)](https://www.codacy.com/app/fmonthel/MyNagiosClientMng?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=fmonthel/MyNagiosClientMng&amp;utm_campaign=Badge_Grade)


Cli to manage add and removal of clients into Nagios

## To list the Nagios Hostgroup(s) :

    python inventory.py --action list-hostgroups
    INFO:MyNagiosClientMng.MncmMotor:Creating an instance of MncmMotor
    INFO:MyNagiosClientMng.MncmMotor:Starting parsing Nagios file "/srv/flaprdmon01/etc/nagios/objects/myhostgroups.cfg"
    INFO:MyNagiosClientMng.MncmMotor:End of parsing Nagios file "/srv/flaprdmon01/etc/nagios/objects/myhostgroups.cfg"
    INFO:MyNagiosClientMng.MncmMotor:Starting parsing Nagios directory "/srv/flaprdmon01/etc/nagios/objects/assets/"
    INFO:MyNagiosClientMng.MncmMotor:End of parsing Nagios directory "/srv/flaprdmon01/etc/nagios/objects/assets/"
    INFO:MyNagiosClientMng:Request to get the Nagios Hostgroup(s) Ascii Table
    ######### DATE : 2017-10-08 - APP : MyNagiosClientMng #########
    - Start time : 2017-10-08 16:14:13
    - Finish time : 2017-10-08 16:14:13
    - Delta time : 0 second(s)
    +-------------------+---------------------+
    | Hostgroup name    | Number of client(s) |
    +-------------------+---------------------+
    | svc-services      |                   6 |
    | ftp-servers       |                   2 |
    | ldap-servers      |                   1 |
    | mysql-servers     |                   1 |
    | ssh-servers       |                  10 |
    | http-servers      |                   1 |
    | ntp-servers       |                   1 |
    | linux-servers     |                   6 |
    | dns-servers       |                   1 |
    | smb-servers       |                   1 |
    | smtp-servers      |                   1 |
    +-------------------+---------------------+
    | Total : 11 row(s) |                     |
    +-------------------+---------------------+

## To list the Nagios Client(s) :

    python inventory.py --action list-clients
    INFO:MyNagiosClientMng.MncmMotor:Creating an instance of MncmMotor
    INFO:MyNagiosClientMng.MncmMotor:Starting parsing Nagios file "/srv/flaprdmon01/etc/nagios/objects/myhostgroups.cfg"
    INFO:MyNagiosClientMng.MncmMotor:End of parsing Nagios file "/srv/flaprdmon01/etc/nagios/objects/myhostgroups.cfg"
    INFO:MyNagiosClientMng.MncmMotor:Starting parsing Nagios directory "/srv/flaprdmon01/etc/nagios/objects/assets/"
    INFO:MyNagiosClientMng.MncmMotor:End of parsing Nagios directory "/srv/flaprdmon01/etc/nagios/objects/assets/"
    INFO:MyNagiosClientMng:Request to get the Nagios client(s) Ascii Table
    ######### DATE : 2017-10-08 - APP : MyNagiosClientMng #########
    - Start time : 2017-10-08 17:51:38
    - Finish time : 2017-10-08 17:51:38
    - Delta time : 0 second(s)
    +---------------------------+---------------------------+----------------+--------------------------------------------------------------------------+
    | Client name               | Address                   | Type           | Nagios Filename                                                          |
    +---------------------------+---------------------------+----------------+--------------------------------------------------------------------------+
    | flaprddns01.flox-arts.in  | flaprddns01.flox-arts.in  | linux-server   | /srv/flaprdmon01/etc/nagios/objects/assets/flaprddns01.flox-arts.in.cfg  |
    | flaprdmon01.flox-arts.in  | flaprdmon01.flox-arts.in  | linux-server   | /srv/flaprdmon01/etc/nagios/objects/assets/flaprdmon01.flox-arts.in.cfg  |
    | marcus.flox-arts.net      | marcus.flox-arts.net      | linux-server   | /srv/flaprdmon01/etc/nagios/objects/assets/marcus.flox-arts.net.cfg      |
    | ap2.flox-arts.in          | ap2.flox-arts.in          | generic-switch | /srv/flaprdmon01/etc/nagios/objects/assets/ap2.flox-arts.in.cfg          |
    +---------------------------+---------------------------+----------------+--------------------------------------------------------------------------+
    | Total : 4 row(s)          |                           |                |                                                                          |
    +---------------------------+---------------------------+----------------+--------------------------------------------------------------------------+
    

## To add Nagios Client :

    python add-client.py --address ap3.flox-arts.in --hosttype generic-switch --hostgroups ssh-servers,ntp-servers
    INFO:MyNagiosClientMng.MncmMotor:Creating an instance of MncmMotor
    INFO:MyNagiosClientMng.MncmMotor:Starting parsing Nagios file "/srv/flaprdmon01/etc/nagios/objects/myhostgroups.cfg"
    INFO:MyNagiosClientMng.MncmMotor:End of parsing Nagios file "/srv/flaprdmon01/etc/nagios/objects/myhostgroups.cfg"
    INFO:MyNagiosClientMng.MncmMotor:Starting parsing Nagios directory "/srv/flaprdmon01/etc/nagios/objects/assets"
    INFO:MyNagiosClientMng.MncmMotor:End of parsing Nagios directory "/srv/flaprdmon01/etc/nagios/objects/assets"
    INFO:MyNagiosClientMng:Check if client "ap3.flox-arts.in" is not already part of this configuration
    INFO:MyNagiosClientMng:Check if hostgroup(s) "['ssh-servers', 'ntp-servers']" is part of this configuration
    INFO:MyNagiosClientMng:Adding client "ap3.flox-arts.in" in the Nagios configuration with hostgroup(s) "['ssh-servers', 'ntp-servers']"
    INFO:MyNagiosClientMng.MncmMotor:Creation of the file "/srv/flaprdmon01/etc/nagios/objects/assets/ap3.flox-arts.in.cfg"
    INFO:MyNagiosClientMng.MncmMotor:Rewrite of the Nagios Hostgroup(s) file "/srv/flaprdmon01/etc/nagios/objects/myhostgroups.cfg"
    INFO:MyNagiosClientMng.MncmMotor:End of rewriting of the Nagios Hostgroup(s) file "/srv/flaprdmon01/etc/nagios/objects/myhostgroups.cfg"
    ######### DATE : 2017-10-08 - APP : MyNagiosClientMng #########
    - Start time : 2017-10-08 23:36:16
    - Finish time : 2017-10-08 23:36:16
    - Delta time : 0 second(s)
    +------------------+----------------+-------------------------+--------+
    | Client address   | Type           | Hostgroup(s)            | Action |
    +------------------+----------------+-------------------------+--------+
    | ap3.flox-arts.in | generic-switch | ssh-servers,ntp-servers | Added  |
    +------------------+----------------+-------------------------+--------+

## To remove Nagios Client :

    python remove-client.py --address ap3.flox-arts.in
    INFO:MyNagiosClientMng.MncmMotor:Creating an instance of MncmMotor
    INFO:MyNagiosClientMng.MncmMotor:Starting parsing Nagios file "/srv/flaprdmon01/etc/nagios/objects/myhostgroups.cfg"
    INFO:MyNagiosClientMng.MncmMotor:End of parsing Nagios file "/srv/flaprdmon01/etc/nagios/objects/myhostgroups.cfg"
    INFO:MyNagiosClientMng.MncmMotor:Starting parsing Nagios directory "/srv/flaprdmon01/etc/nagios/objects/assets"
    INFO:MyNagiosClientMng.MncmMotor:End of parsing Nagios directory "/srv/flaprdmon01/etc/nagios/objects/assets"
    INFO:MyNagiosClientMng:Check if client "ap3.flox-arts.in" is part of this configuration
    INFO:MyNagiosClientMng:Removing client "ap3.flox-arts.in" from the Nagios configuration
    INFO:MyNagiosClientMng.MncmMotor:Deletion of the file "/srv/flaprdmon01/etc/nagios/objects/assets/ap3.flox-arts.in.cfg"
    INFO:MyNagiosClientMng.MncmMotor:Rewrite of the Nagios Hostgroup(s) file "/srv/flaprdmon01/etc/nagios/objects/myhostgroups.cfg"
    INFO:MyNagiosClientMng.MncmMotor:End of rewriting of the Nagios Hostgroup(s) file "/srv/flaprdmon01/etc/nagios/objects/myhostgroups.cfg"
    ######### DATE : 2017-10-08 - APP : MyNagiosClientMng #########
    - Start time : 2017-10-08 23:35:03
    - Finish time : 2017-10-08 23:35:03
    - Delta time : 0 second(s)
    +------------------+---------+
    | Client address   | Action  |
    +------------------+---------+
    | ap3.flox-arts.in | Removed |
    +------------------+---------+