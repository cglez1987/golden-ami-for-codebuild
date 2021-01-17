FROM amazonlinux:latest

# Install terraform 
RUN yum install -y yum-utils
RUN yum-config-manager --add-repo https://rpm.releases.hashicorp.com/AmazonLinux/hashicorp.repo

# Install Terraform
RUN yum update -y && yum install -y terraform && terraform --version

# Install python3

# RUN yum install python3 -y && python3 --version

# Install terraform-compliance
# RUN  pip3 install terraform-compliance