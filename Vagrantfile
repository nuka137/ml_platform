# Run the command: vagrant plugin install vagrant-disksize

Vagrant.configure("2") do |config|

  config.vm.box = "ubuntu/focal64"
  config.vm.box_download_insecure = true

  config.vm.define :"k8s-controlplane-1" do |k8s|
    k8s.vm.hostname = "k8s-controlplane-1"

    k8s.vm.network "private_network", ip: "192.168.56.201"
    k8s.vm.network "private_network", ip: "10.0.2.201", virtualbox__intnet: "NatNetwork"

    k8s.vm.provider "virtualbox" do |vb|
      vb.memory = 4096
      vb.cpus = 2
    end

    k8s.disksize.size = "100GB"

    k8s.vm.provision "ansible_local" do |ansible|
      ansible.playbook = "ansible/kubernetes.yaml"
    end
  end

  # config.vm.define :"k8s-worker-1" do |k8s|
  #   k8s.vm.hostname = "k8s-worker-1"

  #   k8s.vm.network "private_network", ip: "192.168.56.202"
  #   k8s.vm.network "private_network", ip: "10.0.2.202", virtualbox__intnet: "NatNetwork"

  #   k8s.vm.provider "virtualbox" do |vb|
  #     vb.memory = 4096
  #     vb.cpus = 2
  #   end

  #   k8s.disksize.size = "100GB"

  #   # k8s.vm.provision "ansible_kubernetes" do |ansible|
  #   #   ansible.playbook = "ansible/kubernetest.yaml"
  #   # end
  # end

end
