#!/bin/sh

# On Mac
# brew install librsvg
# docs: https://www.systutorials.com/docs/linux/man/1-rsvg-convert/

rsvg-convert output.svg -o output.png -w 600

#-b white -w 1000 -h 1000