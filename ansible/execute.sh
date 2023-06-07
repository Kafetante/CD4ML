#!/bin/sh

ansible-playbook -i inventory.yaml --user=mercuryuser installDocker.yaml -k --ask-become-pass