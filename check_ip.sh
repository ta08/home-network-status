#!/bin/sh

#[ -n "$(diff -q -N $(ls | tail -n 1) <(ip a))"]
if [ -n "$(diff -q -N $(ls | tail -n 1) <(ip a))" ]; then
  ip a > zoo_$(date +%Y%m%d-%H%M%S).log
fi
