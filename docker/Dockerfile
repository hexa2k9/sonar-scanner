FROM alpine:3.23

ARG SONAR_SCANNER_HOME=/opt/sonar-scanner
ARG SONAR_SCANNER_VERSION
ARG UID=1000
ARG GID=1000
ENV JAVA_HOME=/usr/lib/jvm/java-17-openjdk \
    HOME=/tmp \
    XDG_CONFIG_HOME=/tmp \
    SONAR_SCANNER_HOME=${SONAR_SCANNER_HOME} \
    SONAR_USER_HOME=${SONAR_SCANNER_HOME}/.sonar \
    PATH=/opt/java/openjdk/bin:${SONAR_SCANNER_HOME}/bin:${PATH} \
    NODE_PATH=/usr/lib/node_modules \
    SRC_PATH=/usr/src \
    LANG=en_US.UTF-8 \
    LC_ALL=en_US.UTF-8

ADD rootfs /
WORKDIR /opt

RUN set -eux \
    && chmod +x /usr/bin/entrypoint.sh /usr/bin/phpunit-junit-edit.py \
    && addgroup -S -g ${GID} scanner-cli \
    && adduser -S -D -u ${UID} -G scanner-cli scanner-cli \
    && apk add --no-cache --virtual build-dependencies \
        unzip \
    && apk add --no-cache \
        git \
        bash \
        curl \
        py-pip \
        python3 \
        py3-pylint \
        npm \
        shellcheck \
        nodejs \
        musl-locales \
        openjdk17-jre \
        musl-locales-lang \
    && curl -sS -o /opt/sonar-scanner-cli.zip \
        https://binaries.sonarsource.com/Distribution/sonar-scanner-cli/sonar-scanner-cli-${SONAR_SCANNER_VERSION}.zip \
    && unzip sonar-scanner-cli.zip \
    && rm sonar-scanner-cli.zip \
    && mv sonar-scanner-${SONAR_SCANNER_VERSION} ${SONAR_SCANNER_HOME} \
    && mkdir -p "${SRC_PATH}" "${SONAR_USER_HOME}" "${SONAR_USER_HOME}/cache" \
    && chown -R scanner-cli:scanner-cli "${SONAR_SCANNER_HOME}" "${SRC_PATH}" \
    && chmod -R 777 "${SRC_PATH}" "${SONAR_USER_HOME}"

WORKDIR ${SRC_PATH}

ENTRYPOINT ["/usr/bin/entrypoint.sh"]

CMD ["sonar-scanner"]
