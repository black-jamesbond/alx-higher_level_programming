#!/bin/bash
#to get the size displaed in bytes

curl -sI "$1" | grep "Content-Length:" | cut -d' ' -f2 
