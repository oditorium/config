#!/bin/bash
pushd "$(dirname "$0")"
pwd

echo "************************************"
echo RUNNING "$0"
echo "************************************"
echo "$0" >> ~/install.log

# https://stackoverflow.com/questions/26193654/node-js-catch-enomem-error-thrown-after-spawn

fallocate -l 4G /swapfile
chmod 600 /swapfile
mkswap /swapfile
swapon /swapfile
echo "/swapfile none swap sw 0 0" | sudo tee -a /etc/fstab

popd
