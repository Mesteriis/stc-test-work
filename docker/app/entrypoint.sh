#!/bin/bash

set -o errexit
set -o pipefail
set -o nounset

alembic -x data=true upgrade head
exec "$@"
