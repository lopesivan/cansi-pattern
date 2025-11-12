#!/usr/bin/env bash

test -n "$DEBUG" && set -x

#                      __ __       ___
#                     /\ \\ \    /'___`\
#                     \ \ \\ \  /\_\ /\ \
#                      \ \ \\ \_\/_/// /__
#                       \ \__ ,__\ // /_\ \
#                        \/_/\_\_//\______/
#                           \/_/  \/_____/
#                                         Algoritimos
#
#
#      Author: Ivan Lopes
#        Mail: ivan@42algoritmos.com.br
#        Site: http://www.42algoritmos.com.br
#     License: gpl
#       Phone: +1 561 801 7985
#    Language: Shell Script
#        File: cheetah.sh
#        Date: Ter 21 Nov 2017 13:27:10 -02
# Description:
# ----------------------------------------------------------------------------
# Modo strict
#set -euo pipefail
# ----------------------------------------------------------------------------

##############################################################################
##############################################################################
##############################################################################

# ----------------------------------------------------------------------------
# Run!
rm *.c *.h

ADT=/workspace/cansi-pattern/cansi-pattern-state
APP=${ADT}/w/v/app.py
YML=state.yml

python ${APP} -s -y ${YML} | sort

find . -maxdepth 1 -name \*.c -o -name \*.h |
    xargs astyle \
        --pad-first-paren-out \
        --style=linux \
        -A1 \
        --indent=spaces=4 \
        --convert-tabs

rm *.orig
pwd
# ----------------------------------------------------------------------------
exit 0
