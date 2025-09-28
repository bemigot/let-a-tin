#!/bin/sh

. ../.env
: "${CF_API_TOKEN:?"Error: CF_API_TOKEN is not set or is empty."}"
AUTH="Authorization: Bearer $CF_API_TOKEN"

if ! command -v jq >/dev/null 2>&1; then
  echo "jq not found or is not executable" >&2
  exit 1
fi

CF_ID=$(curl -s "https://api.cloudflare.com/client/v4/accounts/" -H "$AUTH" | jq -r '.result[0].id')

curl "https://api.cloudflare.com/client/v4/accounts/$CF_ID/tokens/verify" -H "$AUTH"

: "${CLOUDFLARE_EMAIL:?"Error: CLOUDFLARE_EMAIL is not set or is empty."}"
printf "\n\nDNS Zones managed with this token issued for %s\n" "$CLOUDFLARE_EMAIL"
curl https://api.cloudflare.com/client/v4/zones -H "$AUTH" \
   -H "X-Auth-Email: $CLOUDFLARE_EMAIL"
echo
