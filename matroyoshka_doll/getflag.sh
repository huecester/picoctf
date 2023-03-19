#!/bin/bash
rm -rf _dolls*
binwalk -Meq dolls.jpg
cat _dolls.jpg.extracted/base_images/_2_c.jpg.extracted/base_images/_3_c.jpg.extracted/base_images/_4_c.jpg.extracted/flag.txt
