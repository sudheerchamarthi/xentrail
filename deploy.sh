#!/bin/bash
aws eks --region ${AWS_REGION} update-kubeconfig --name ${EKS_CLUSTER}
echo "Deploying now"
kubectl apply -f ./mysql
kubectl apply -f ./webapp