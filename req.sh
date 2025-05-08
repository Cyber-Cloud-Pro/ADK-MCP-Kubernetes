#!/bin/bash
set -e

echo "==== Updating System ===="
sudo apt update && sudo apt upgrade -y

echo "==== Installing Docker ===="
sudo apt install -y docker.io
sudo systemctl start docker
sudo systemctl enable docker
sudo usermod -aG docker $USER

echo "==== Installing Node.js, npm, and npx ===="
curl -fsSL https://deb.nodesource.com/setup_18.x | sudo -E bash -
sudo apt install -y nodejs

echo "Node.js version: $(node -v)"
echo "npm version: $(npm -v)"
echo "npx version: $(npx -v)"

echo "==== Installing Minikube ===="
curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64
sudo install minikube-linux-amd64 /usr/local/bin/minikube
rm minikube-linux-amd64

echo "Minikube version: $(minikube version)"

echo "==== Installing kubectl ===="
sudo snap install kubectl --classic
echo "kubectl version: $(kubectl version --client --short)"

echo "==== All tools installed successfully. You may need to log out and back in for Docker group changes to take effect. ===="
