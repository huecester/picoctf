#!/bin/bash
exiftool cat.jpg | grep License | cut -d ':' -f 2 | sed -e 's/ //g' | base64 -d
