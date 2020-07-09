FROM centos:7
ENV LC_ALL en_US.UTF-8
ENV TZ=Asia/Shanghai

COPY . /webapp
WORKDIR /webapp/conf

RUN mv CentOS-Base.repo /etc/yum.repos.d/CentOS-Base.repo \
	&& yum clean all \
	&& yum makecache \
	&& yum install -y iproute vim curl wget tree gcc python3-devel python3-pip python3-wheel \
	&& mv .vimrc /root \
	&& ln -sf /usr/bin/vim /usr/bin/vi \
	&& mkdir /root/.pip \
	&& mv pip.conf /root/.pip/ \
	&& yum clean all 

RUN python3 -m pip install -U pip \
	&& python3 -m pip install -r requirements.txt \
	&& rm -rf /webapp/conf

WORKDIR /webapp

CMD ["uwsgi", "--ini", "/webapp/uwsgi.ini"]
