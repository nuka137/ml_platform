# ml_platform

* Setup VMs with kubernetes ready environment.

```
vagrant up
```

* Check if all VMs can be connected correctly.

```
ansible all -m ping -i inventory.ini --private-key=~/.ssh/id_rsa
```

* Setup Kuberntes cluster

```
ansible-playbook -i inventory.ini ansible/setup_kubernetes_cluster.yaml --private-key=~/.ssh/id_rsa
```

* Install Kubeflow

```
ansible-playbook -i inventory.ini ansible/setup_kubeflow.yaml --private-key=~/.ssh/id_rsa
```

* Install Airflow

```
ansible-playbook -i inventory.ini ansible/setup_airflow.yaml --private-key=~/.ssh/id_rsa
```


* https://stackoverflow.com/questions/63917524/helm-postgres-password-authentication-failed