#!/bin/bash

for n in {1..25}; do
    printf "<HTML><HEAD><META HTTP-EQUIV=REFRESH CONTENT=\"1; URL=http://github.com/HampshireCS/CS112-Spring2012/tree/master/hw%02d\"></HEAD></HTML>"  $n> hw$n.html
done
