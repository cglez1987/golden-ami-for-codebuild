FROM 137112412989.dkr.ecr.us-east-1.amazonaws.com/amazonlinux:latest

RUN yum install -y unzip
RUN curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip" && unzip awscliv2.zip
RUN ./aws/install

terraform# Install  
RUN yum install -y yum-utils
RUN yum-config-manager --add-repo https://rpm.releases.hashicorp.com/AmazonLinux/hashicorp.repo
RUN yum update -y && yum install -y terraform && terraform --version

# Install python3

# RUN yum install python3 -y && python3 --version

# Install terraform-compliance
# RUN  pip3 install terraform-compliance