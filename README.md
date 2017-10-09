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