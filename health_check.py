#!/usr/bin/env python
import os, sys, shutil, psutil, socket, sys
sys.path.insert(1, r'C:\Users\jhoov\Projects\FruitStand')
import send_email

def check_localhost():
    '''Returns True if localhost does not resolve to 127.0.0.1, otherwise
    False'''
    host = socket.gethostbyname('localhost')
    if host == '127.0.0.1':
        return False
    return True

def check_memory(min_mem=500):
    '''
    Returns True if there is less than 500MB of memory available,
    otherwise False.
    '''
    mem = psutil.virtual_memory()
    memck = min_mem * 1024 * 1024
    if mem.free < memck:
        #print(f'There is {pct_free:.2f}% free memory.')
        return True
    return False

def check_reboot():
    '''Returns True if the computer has a pending re-boot'''
    return os.path.exists('/run/reboot-required')

def check_disk_usage(disk, min_pct):
    '''Returns True if there isn't enough disk space, False otherwise'''
    du = shutil.disk_usage(disk)
    pct_free = 100 * du.free / du.total  #Not currently using this check
    gb_free = du.free / 2**30 # 2**30 converts to GB
    #print(f'Pct Free: {pct_free:.2f}\nGB Free: {gb_free:.2f}')
    if pct_free < min_pct: # or gb_free < min_gb:
        #print (f'There is {pct_free:.2f}% free space and {gb_free:.2f} GB free.')
        return True
    return False

def check_cpu(max_pct=80):
    '''
    Make sure the CPUs are not running at > 80% capacity. Return True
    if they are, otherwise return False.
    '''
    cpu = psutil.cpu_percent()
    if cpu > max_pct:
        return True
    return False

def check_root_full():
    '''returns True if the root partition is full, False otherwise'''
    return check_disk_usage(disk='/',min_pct=20)

def main():
    '''
    Create a list of checks to perform along with the message that should
    be returned if the check fails. Each check that fails should be emailed
    out to a specific user.
    '''
    checks = [
            (check_root_full, 'Error - Available disk space is less than 20%'),
            (check_memory, 'Error - Available memory is less than 500MB'),
            (check_cpu, 'Error - CPU usage is over 80%'),
            (check_localhost, 'Error - localhost cannot be resolved to 127.0.0.1'),
            ]
    everything_ok = True
    for check, msg in checks:
        if check():
            subject = msg
            body = 'Please check your system and resolve the issue as soon as possible.'
            sender = 'automation@example.com'
            recipient = '<user>@example.com'
            message = send_email.generate_email(sender, recipient, subject, body)
            print(message)
            everything_ok = False
    if not everything_ok:
        return 1
        #sys.exit(1)

    print('Everything is OK.')
    return 0
    sys.exit(0)

main()
