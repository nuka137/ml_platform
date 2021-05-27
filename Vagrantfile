# Run the command: vagrant plugin install vagrant-disksize

Vagrant.configure("2") do |config|

  config.vm.box = "ubuntu/focal64"
  config.vm.box_download_insecure = true
  config.vm.synced_folder ".", "/vagrant", :mount_options => ["dmode=775", "fmode=664"]

  config.ssh.insert_key = false
  config.ssh.private_key_path = "~/.vagrant.d/insecure_private_key"
  config.vm.provision "file", source: "~/.vagrant.d/insecure_private_key", destination: "/home/vagrant/.ssh/id_rsa"
  config.vm.provision "shell", privileged: false, inline: <<-SHELL
    chmod 600 /home/vagrant/.ssh/id_rsa
  SHELL

  config.vm.define :"k8s-controlplane-1" do |k8s|
    k8s.vm.hostname = "k8s-controlplane-1"

    k8s.vm.network "private_network", ip: "192.168.56.201"
    k8s.vm.network "private_network", ip: "10.0.11.201", virtualbox__intnet: "NatNetwork"

    k8s.vm.provider "virtualbox" do |vb|
      vb.memory = 4096
      vb.cpus = 4
    end

    k8s.disksize.size = "100GB"

    k8s.vm.provision "ansible_local" do |ansible|
      ansible.playbook = "ansible/setup_kubernetes_node.yaml"
      ansible.inventory_path = "inventory.ini"
      ansible.limit = "controlplane"
    end
  end

  (1..1).each do |i|
    config.vm.define :"k8s-worker-#{i}" do |k8s|
      k8s.vm.hostname = "k8s-worker-#{i}"

      k8s.vm.network "private_network", ip: "192.168.56.21#{i}"
      k8s.vm.network "private_network", ip: "10.0.11.21#{i}", virtualbox__intnet: "NatNetwork"

      k8s.vm.provider "virtualbox" do |vb|
        vb.memory = 8192
        vb.cpus = 4
      end

      k8s.disksize.size = "100GB"

      k8s.vm.provision "ansible_local" do |ansible|
        ansible.playbook = "ansible/setup_kubernetes_node.yaml"
        ansible.inventory_path = "inventory.ini"
        ansible.limit = "worker"
      end
    end
  end

  config.vm.define :"k8s-nfs-server" do |k8s|
    k8s.vm.hostname = "k8s-nfs-server"

    k8s.vm.network "private_network", ip: "192.168.56.221"
    k8s.vm.network "private_network", ip: "10.0.11.221", virtualbox__intnet: "NatNetwork"

    k8s.vm.provider "virtualbox" do |vb|
      vb.memory = 1024
      vb.cpus = 1
    end

    k8s.disksize.size = "150GB"

    k8s.vm.provision "ansible_local" do |ansible|
      ansible.playbook = "ansible/setup_nfs_server.yaml"
      ansible.inventory_path = "inventory.ini"
      ansible.limit = "nfs"
    end
  end

end
