# UpPwn

### Version 0.1 [Dev in progress]

## About The Project

UpPwn is a script that automate detection of security flaws on websites' file upload systems.
In some cases it also allows to exploit these vulnerabilities in order to upload malicious files.

## Requirements
* Python 2.7
* Firefox with the Selenium IDE plugin (http://www.seleniumhq.org/projects/ide/)
* GNU/Linux system

Testing is done only with [GNU/Linux Ubuntu](http://www.ubuntu.com/) 16.04 LTS stable and [Debian](https://www.debian.org/index.fr.html) Jessie.

## Installation
    sudo apt-get install python-pip
    pip install --upgrade pip
    git clone https://github.com/ferrery1/UpPwn.git && cd UpPwn
    pip2 install -r requirements.lst
    tar -zxvf misc/firefox_profile.up.tar.gz -C misc/

## Usage

python UpPwn.py [-h/--help] ; pyclean .
