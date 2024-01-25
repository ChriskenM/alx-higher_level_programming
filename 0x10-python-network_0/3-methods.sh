#!/bin/bash
#Displays all the accepted HTTP Methods
curl -sI "$1" | grep "Allow" | cut -d " " -f 2-
