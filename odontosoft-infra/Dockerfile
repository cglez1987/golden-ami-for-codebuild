FROM amazonlinux:latest

# Install terraform 
RUN yum install -y yum-utils
RUN yum-config-manager --add-repo https://rpm.releases.hashicorp.com/AmazonLinux/hashicorp.repo
RUN yum update -y && yum install -y terraform 
RUN terraform -version

# Install python3

RUN yum install python3 -y
RUN python3 --version
RUN  pip3 install terraform-compliance