#!/bin/bash

echo "===================="
echo "Updating apt..."
curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key add -
apt-get update
if [ $? -ne 0 ]; then
  echo "Updating apt failed!"
  exit 1
fi

echo "===================="
echo "Installing Python 3 Package Manager..."
apt-get install -y python3 python3-pip
if [ $? -ne 0 ]; then
  echo "Installing Python 3 Package Manager failed!"
  exit 1
fi

echo "===================="
echo "Upgrading Python 3 Package Manager..."
python3 -m pip install --upgrade pip
if [ $? -ne 0 ]; then
  echo "Upgrading Python 3 Package Manager failed!"
  exit 1
fi
pip3 install --upgrade setuptools
if [ $? -ne 0 ]; then
  echo "Upgrading Python 3 Setup Tools failed!"
  exit 1
fi

echo "===================="
echo "Installing Python 3 dependencies..."
pip3 install --upgrade --requirement src/requirements.txt
if [ $? -ne 0 ]; then
  echo "Installing Python 3 dependencies failed!"
  exit 1
fi
