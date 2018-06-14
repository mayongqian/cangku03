#Filename: backup_ver1.py
import os 
import time
#1. The files and directories to be backed up arespecified in a list.
source = ['/var/log/jenkins/jenkins.log']
# If you are using Windows, use source =[r'C:\Documents', r'D:\Work'] or something like that
# 2. The backup must be stored in a main backupdirectory
target_dir='/var/lib/jenkins/Backupfile'
# Remember to change thisto what you will be using
# 3. The files are backed up into a zip file.
# 4. The name of the zip archive is the current date andtime
target=target_dir+'/'+time.strftime('%Y%m%d%H%M%S')+'.zip'
# 5. We use the zip command (in Unix/Linux) to put thefiles in a zip archive
zip_command="zip -qr '%s' %s"%(target, ' '.join(source))
#Run the backp
if os.system(zip_command)==0:
    print ('Successful backup to',target)
else:
    print ('Backup FAILED')
print (target)
print (zip_command)
