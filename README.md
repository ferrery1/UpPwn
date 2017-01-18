# UpPwn

### Version 0.1 [Dev in progress]

## About

UpPwn is a script that automate detection of security flaws on websites' file upload systems.
In some cases it also allows to exploit these vulnerabilities in order to upload malicious files.

## Requirements
* Python 2.7
* Nodejs / Phantomjs
* GNU/Linux system

Testing is done only with [GNU/Linux Ubuntu](http://www.ubuntu.com/) 16.04 LTS stable and [Debian](https://www.debian.org/index.fr.html) Jessie.

## Installation
    curl -sL https://deb.nodesource.com/setup_6.x | sudo -E bash -
    sudo apt-get install nodejs
    sudo npm install phantomjs-prebuilt
    sudo apt-get install python-pip
    pip install --upgrade pip
    git clone https://github.com/ferrery1/UpPwn.git && cd UpPwn
    pip2 install -r requirements.lst

## Usage

python UpPwn.py [-h/--help] ; pyclean .
