#!/bin/sed

s/^\s+//
1s/(.+?):/RUN REPORT: \1\n/
/-{10}/d
