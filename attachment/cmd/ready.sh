#!/bin/sh -xe
echo "run ready"
#https://qiita.com/yohm/items/047b2e68d008ebb0f001
#https://qiita.com/yohm/items/047b2e68d008ebb0f001
#USER_ID=${LOCAL_UID:-9001}
#GROUP_ID=${LOCAL_GID:-9001}

#echo "Starting with UID : $USER_ID, GID: $GROUP_ID"
#useradd -u $USER_ID -o -m user
#groupmod -g $GROUP_ID user
#export HOME=/home/user

#exec /usr/sbin/gosu user "$@"

#USER_ID=${LOCAL_UID:-9001}
#GROUP_ID=${LOCAL_GID:-9001}

#echo "Starting with UID : $USER_ID, GID: $GROUP_ID"
#useradd -u $USER_ID -o -m user
#groupmod -g $GROUP_ID user
#export HOME=/home/user

#exec /usr/sbin/gosu user "$@"

#adduser -S $HOST_USER_NAME

#mkdir /home/$HOST_USER_NAME
#su - $HOST_USER_NAME


echo "this is $HOST_USER_NAME"
adduser -D -u 1000 $HOST_USER_NAME
echo "$HOST_USER_NAME ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers
echo "%sudo   ALL=(ALL:ALL) NOPASSWD: ALL" >> /etc/sudoers

echo "$HOST_USER_NAME:$HOST_USER_NAME" | chpasswd