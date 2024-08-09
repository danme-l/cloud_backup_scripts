# Python Script for cloud backups
Uses [Rclone](https://rclone.org/) to automatically sync a local directory to a cloud storage provider. 

Usage: `python sync_remote.py [/path/to/local/folder] [rclone_remote_name] [path/to/cloud/dest/folder]`

Alternativaly, you use the bash script. Make it executable like this: `chmod +x my_backup.sh`, and then copy or move it to somewhere on your path. I moved mine to /usr/local/bin

Since it uses RClone cli commands, you'll need to configure Rclone for your cloud storage provider. I use Mega, no guarantees it works with others (but it should).