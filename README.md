# MyNagiosClientMng

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/296734d54ebc4a608328c887225114f9)](https://www.codacy.com/app/fmonthel/MyNagiosClientMng?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=fmonthel/MyNagiosClientMng&amp;utm_campaign=Badge_Grade)


Cli to manage add and removal of clients into Nagios

## To list the Nagios Hostgroup(s) :

    python motor.py --action list-hostgroups
    INFO:MyNagiosClientMng.MncmMotor:Creating an instance of MncmMotor
    INFO:MyNagiosClientMng.MncmMotor:Starting parsing Nagios file "/tmp/myhostgroups.cfg
    INFO:MyNagiosClientMng.MncmMotor:End of parsing Nagios file "/tmp/myhostgroups.cfg
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
