#!/bin/bash

for n in {1..25}; do
    echo "<HTML><HEAD><META HTTP-EQUIVE=REFRESH CONTENT=\"1; URL=http://github.com/HampshireCS/cs112-spring12/tree/master/hw$n\"></HEAD></HTML>" > hw$n.html
done
