#!/bin/bash

set -e

cat requirements.txt
find . -name "requirements.txt" -print0 | xargs -0 cat
