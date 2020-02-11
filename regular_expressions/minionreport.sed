#!/bin/sed

s/^\s+//
1s/(.+?):/RUN REPORT: \1\n/
/-{10}/d
/^[a-z]+_\|/d
/p?changes:/d
/^[a-z_]+:/ {
N
s/\n\s+/ /
}
