FROM    postgres:11.4-alpine

# ADD Timezone
RUN     apk add tzdata \
        && echo "America/Sao_Paulo" > /etc/timezone

# RUN create.sql on init
ADD     ./create.sql /docker-entrypoint-initdb.d