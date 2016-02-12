
FROM ubuntu:latest
MAINTAINER Nils Schmidt <schmidt89@informatik.uni-marburg.de>

ENV WORK_DIR /home/meshadmin
ENV HOME $WORK_DIR
ENV SERVAL_REPO https://github.com/umr-studenten/serval-dna.git
ENV SERVAL_TESTS https://github.com/gh0st42/serval-tests.git
ENV CORE_SERVAL https://github.com/gh0st42/core-serval.git

#####################################################
### Installation
#####################################################

RUN apt-get update \
	&& apt-get install -y autoconf gcc\
	&& apt-get install -y core-network git make\
	&& apt-get clean
	
RUN mkdir -p $WORK_DIR
WORKDIR $WORK_DIR

RUN mkdir -p $WORK_DIR/.core\
	&& cd $WORK_DIR\
	&& git clone $CORE_SERVAL\
	&& git clone $SERVAL_TESTS\
	&& mv core-serval/dotcore/* $WORK_DIR/.core/\
	&& mkdir serval-conf\
	&& git clone $SERVAL_REPO\
	&& cd serval-dna\
	&& autoreconf -i\
	&& ./configure --prefix=/home/meshadmin/serval-conf\
	&& make -j 2\
	&& make install\
	&& cd ..\
	&& ln -s $WORK_DIR/serval-dna/servald /usr/bin/servald\
	&& echo "custom_services_dir =$WORK_DIR/.core/myservices" >> /etc/core/core.conf\
	&& service core-daemon restart

ADD . $WORK_DIR

ENV PATH $PATH:$WORK_DIR/serval-conf/sbin/
CMD ./docker_start.sh
