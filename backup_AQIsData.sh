# backup AQIsData by zip and log the information to file backup.log
cd /home/yb77423/AQI && zip -r ../backup_AQIsData.zip AQIsData/ && echo $(date --rfc-3339=seconds)' | Successfully backup to backup_AQIsData.zip' >>backup.log  || echo $(date --rfc-3339=seconds)' | Fail to backup to backup_AQIsData.zip' >>backup.log


