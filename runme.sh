#!/bin/bash
sudo mkdir /usr/PiPwmCLI
sudo mv PiPwmCLI.py /usr/PiPwmCLI
sudo mv pipwm.sh /usr/bin
sudo chmod +x /usr/bin/pipwm.sh
alias pipwm="/usr/bin/pipwm.sh"