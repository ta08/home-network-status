#!/bin/sh

if [ -n "$(diff -q -N $(ls | tail -n 1) <(arp -a))" ]; then
  arp -a > zoo_$(date +%Y%m%d-%H%M%S).log
fi
