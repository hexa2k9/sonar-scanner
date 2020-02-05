FROM debian:stretch-slim

ARG SONAR_SCANNER_HOME=/opt/sonar-scanner
ARG NODEJS_HOME=/opt/nodejs
ARG NODEJS_VERSION=v10.16.3
ARG SONAR_SCANNER_VERSION=4.2.0.1873

ENV SONAR_SCANNER_HOME=${SONAR_SCANNER_HOME} \
    NODEJS_HOME=${NODEJS_HOME} \
    PATH=${SONAR_SCANNER_HOME}/bin:${NODEJS_HOME}/bin:${PATH} \
    NODE_PATH=${NODEJS_HOME}/lib/node_modules

RUN apt-get update \
    && apt-get install -y --no-install-recommends ca-certificates git wget unzip xz-utils pylint locales \
    && rm -rf /var/lib/apt/lists/*

RUN printf "en_US.UTF-8 UTF-8\n" | tee -a /etc/locale.gen \
    && locale-gen \
    && ln -nsf /usr/share/zoneinfo/UTC /etc/localtime \
    && dpkg-reconfigure tzdata

ENV LANG en_US.UTF-8
ENV LC_ALL en_US.UTF-8

WORKDIR /opt
RUN wget -q -O /opt/sonar-scanner-cli.zip https://binaries.sonarsource.com/Distribution/sonar-scanner-cli/sonar-scanner-cli-${SONAR_SCANNER_VERSION}-linux.zip \
    && unzip sonar-scanner-cli.zip \
    && rm sonar-scanner-cli.zip \
    && mv sonar-scanner-${SONAR_SCANNER_VERSION}-linux ${SONAR_SCANNER_HOME} \
    && wget -q -O nodejs.tar.xz https://nodejs.org/dist/${NODEJS_VERSION}/node-${NODEJS_VERSION}-linux-x64.tar.xz \
    && tar Jxf nodejs.tar.xz \
    && rm nodejs.tar.xz \
    && mv node-${NODEJS_VERSION}-linux-x64 ${NODEJS_HOME} \
    && npm install -g typescript@3.7.5

WORKDIR /usr/src

ENTRYPOINT ["/usr/bin/entrypoint.sh"]
