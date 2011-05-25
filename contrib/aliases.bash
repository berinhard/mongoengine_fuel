#!/bin/bash
alias run_tests="nosetests -s -w $VIRTUAL_ENV --all-modules --with-id -i '^(it|ensure|must|should|deve|garante|assegura)' --id-file='$VIRTUAL_ENV/.noseids' -v"

alias cdmongoengine="cd `virtualenvwrapper_get_site_packages_dir`/mongoengine"
