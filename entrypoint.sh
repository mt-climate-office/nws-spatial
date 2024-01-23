#!/bin/sh
env >> ~/env.log
echo 'PATH=/usr/local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin' > /etc/crontab
echo 'SHELL=/bin/bash' >> /etc/crontab
# Run hourly every hour at 15-min mark
echo '*/15 * * * * root bash -c "source $HOME/env.log; python /app/main.py zones alerts templates"' >> /etc/crontab

# start cron
service cron start
tail -f /dev/null