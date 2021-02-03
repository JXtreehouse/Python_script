import os
logdir = os.getenv('logs')
logfile = 'script_list.log'
path = os.getenv("scripts")

logfilename = os.path.join(logdir, logfile)
log = open(logfilename, 'w')

temp = os.walk(path)
for dirpath, dirname, filenames in os.walk(path):
    for filename in filenames:
        log.write(os.path.join(dirpath, filename) + '\n')


print("\nYour logfile ", logfilename, "has been created")