kubectl get namespaces
kubectl create -f namespace.yaml 
kubectl get namespace
kubectl get namespace --show-labels
kubectl config set-context dev --namespace=development
kubectl config view
kubectl config use-context dev
kubectl config current-context
