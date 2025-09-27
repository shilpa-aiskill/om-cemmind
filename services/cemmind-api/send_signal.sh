#!/bin/bash
curl -X POST "https://cemmind-api-7pkrptdbbq-uc.a.run.app/api/v1/kiln/act" \
  -H "Content-Type: application/json" \
  -d '{
    "readings": [
      {"tag": "kiln.inlet.temp", "value": 1350, "unit": "C"},
      {"tag": "kiln.o2.exit", "value": 2.5, "unit": "%"}
    ],
    "meta": {"source": "auto-simulated"}
  }'
