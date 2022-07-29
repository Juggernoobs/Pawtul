echo "for x in $(ps -ef | grep flask | awk '{print $2}'); do kill -9 $x; done"
