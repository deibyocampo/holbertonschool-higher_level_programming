#!/bin/bash
#displays the size of the body
curl -s -o /dev/null --write-out "%{size_download}\n" "$1"
