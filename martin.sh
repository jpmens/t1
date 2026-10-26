#!/bin/bash

figlet "Hello!"

echo ""
echo "Semaphore env variables:"
env | grep SEMAPHORE | sed -e 's/^/   /'

echo "+++ --- here we go!"
echo "Your $INSTALLTYPE is complete"
