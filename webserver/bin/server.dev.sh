#!/bin/bash

set -e

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
pushd $DIR/..

# flask run -h 0.0.0.0 -p ${PORT}
honcho start web

popd
