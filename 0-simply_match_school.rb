#!/usr/bin/env ruby
input = ARGV[0]
regex = /Schoo/
matches = input.scan(regex).join
print matches
