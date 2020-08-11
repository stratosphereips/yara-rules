#!/bin/bash
URL='http://ipverse.net/ipblocks/data/countries/{country}-ipv6.zone'
OUT="countries"

[ ! -d "${OUT}" ] && mkdir $OUT
for l1 in {a..z};do
  for l2 in {a..z};do
    URLCR=${URL/\{country\}/${l1}${l2}}
    NAME=$( sed -E 's/^.+\/(.+)$/\1/'<<<$URLCR )
    curl -fsS -o ${OUT}/${NAME} ${URLCR} >&/dev/null && \
      echo "[+] IPv6 range for country ${l1}${l2}"
  done
done
