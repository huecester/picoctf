#!/bin/bash
curl -sI http://mercury.picoctf.net:53554/index.php | grep flag | cut -d ' ' -f '2'
