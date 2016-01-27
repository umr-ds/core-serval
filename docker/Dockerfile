
FROM ubuntu:latest
MAINTAINER Nils Schmidt <schmidt89@informatik.uni-marburg.de>

ENV WORK_DIR /home/meshadmin
ENV HOME $WORK_DIR
ENV SERVAL_REPO https://github.com/umr-studenten/serval-dna.git

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
	&& git clone https://github.com/gh0st42/core-serval.git\
	&& mv core-serval/dotcore/* $WORK_DIR/.core/\
	&& mkdir serval-conf\
	&& git clone $SERVAL_REPO\
	&& cd serval-dna\
	&& autoreconf -i\
	&& ./configure --prefix=/home/meshadmin/serval-conf\
	&& make -j 2\
	&& make install\
	&& service core-daemon restart

ADD . $WORK_DIR

ENV PATH $PATH:/home/meshadmin/serval-conf/sbin/
CMD ./docker_start.sh
