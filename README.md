# ml_platform

```
vagrant up
```



```
ansible all -m ping -i inventory.ini --private-key=~/.ssh/id_rsa
```

```
ansible-playbook -i inventory.ini ansible/setup_kubernetes_cluster.yaml --private-key=~/.ssh/id_rsa
```

```
ansible-playbook -i inventory.ini ansible/setup_kubeflow.yaml --private-key=~/.ssh/id_rsa
```