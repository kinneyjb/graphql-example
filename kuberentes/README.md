## use helm with minikube

First build the image:

```bash
$ cd ../docker
$ eval "$(minikube docker-env)"
$ docker-compose build
```

Then use helm to install the helm-chart:

```bash
$ cd ../kubernetes
$ helm install helm-chart
```

Then find the service name and open the url using minikube:

```bash
$ SERVICE_NAME=$(kubectl get service -l app.kubernetes.io/name=helm-chart -o jsonpath="{.items[*].metadata.name}")
$ open "$(minikube service $SERVICE_NAME --url)/graphql"
```

In the graphql ui run the following:

```
{
  allDatasets {
    edges {
      node {
        name
        granules {
          edges {
            node {
              name
            }
          }
        }
      }
    }
  }
}

```
