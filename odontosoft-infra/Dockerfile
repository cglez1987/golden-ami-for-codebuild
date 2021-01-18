FROM 137112412989.dkr.ecr.us-east-1.amazonaws.com/amazonlinux:latest

#Install aws-cli
RUN yum install -y unzip
RUN curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip" && unzip awscliv2.zip && ./aws/install

# Install terraform
RUN yum install -y yum-utils git
RUN yum-config-manager --add-repo https://rpm.releases.hashicorp.com/AmazonLinux/hashicorp.repo
RUN yum update -y && yum install -y terraform && terraform --version

# Install python3

# RUN yum install python3 -y && python3 --version

# Install terraform-compliance
# RUN  pip3 install terraform-compliance