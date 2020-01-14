#!/bin/bash
#display the size the body of the response
curl -sX POST -d "email=hr@holbertonschool.com&subject=I will always be here for PLD" "$1"
