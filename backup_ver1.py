#!/usr/bin/python

# 给所有重要文件建立备份

import os
import time

# The file and directories to be backed up are specified in a list.
source = ['"D:\\workspace\\clion"', 'D:\\workspace\\R']
# Notice we had to use double quotes inside the string for names with spaces in it.

# The backup must be stored in a main backup directory
target_dir = 'D:\\Backup'

# The files are backed up into zip file
# The name of the zip archive is the current date and time
target = target_dir + os.sep + time.strftime('%Y%m%d%H%M%S') + '.zip'

# we use the zip command to put the files in a zip archive
zip_command = "zip -ar {0} {1}".format(target, ' '.join(source))

# Run the backup
print(zip_command)
if os.system(zip_command) == 0:
    print('Successful backup to', target)
else:
    print('Backup FAILED')
    print('备份出错！')