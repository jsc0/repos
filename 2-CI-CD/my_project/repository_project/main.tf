provider "aws" {
  region = "us-east-1"
}

resource "aws_instance" "jenkins_qa_staging" {
  ami           = "ami-0c94855ba95c71c99"  # Ubuntu 20.04 LTS
  instance_type = "t2.micro"
  key_name      = "your_key_pair_name"
  security_group_ids = ["your_security_group_id"]
  subnet_id     = "your_subnet_id"

  user_data = <<-EOF
    #!/bin/bash

    # Install Jenkins
    wget -q -O - https://pkg.jenkins.io/debian/jenkins.io.key | sudo apt-key add -
    sudo sh -c 'echo deb http://pkg.jenkins.io/debian-stable binary/ > /etc/apt/sources.list.d/jenkins.list'
    sudo apt-get update && sudo apt-get install -y jenkins

    # Install QA and Staging tools
    # Add your necessary installation steps for QA and Staging tools here

    EOF

  tags = {
    Name = "jenkins-qa-staging-server"
  }
}

resource "aws_instance" "prod_db" {
  ami           = "ami-0c94855ba95c71c99"  # Ubuntu 20.04 LTS
  instance_type = "t2.micro"
  key_name      = "your_key_pair_name"
  security_group_ids = ["your_security_group_id"]
  subnet_id     = "your_subnet_id"

  user_data = <<-EOF
    #!/bin/bash

    # Install Production and Database tools
    # Add your necessary installation steps for Production and Database tools here

    EOF

  tags = {
    Name = "prod-db-server"
  }
}
