#!/bin/bash

cd /src/frontend \
    && npm i \
    && npx webpack ./client.js --mode=production