console output
description "Sample basestation http server"
author  "Aitor Gomez-Goiri <aitor.gomez@deusto.es>"

setuid {{execuser}}

# http://askubuntu.com/questions/47649/does-upstart-emit-hooks-for-sysv-jobs
start on runlevel [2345] # E.g., /etc/rc2.d/S91apache2 exists
stop on runlevel [016]   # E.g., /etc/rc0.d/K09apache2 exists

env VIRTUALENV_BIN={{pyhome}}/bin

chdir /home/{{execuser}}/

exec $VIRTUALENV_BIN/python $VIRTUALENV_BIN/weblab-admin start {{instancedir}}