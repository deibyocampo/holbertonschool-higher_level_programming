#!/bin/bash
#displays the size of the body of the response
curl -sI "$1" | grep -o "Allow.*" | cut -d: -f2- | cut -d' ' -f2-
