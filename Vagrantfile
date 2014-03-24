VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  config.vm.box = "hashicorp/precise64"
  config.vm.network "forwarded_port", guest:80, 
                    host:8080, auto_correct:true  
  config.vm.network "forwarded_port", guest:8000, 
                    host:8000, auto_correct:true
  config.vm.boot_timeout = 300
  config.vm.graceful_halt_timeout = 300

  config.vm.provider "virtualbox" do |v|
    v.name ="sample_vm"
    v.memory = 384
    v.customize ["modifyvm", :id, "--cpuexecutioncap", "90"]
    v.gui = false
  end

  config.vm.provision :puppet do |p|
  	p.manifests_path ="manifests"
  	p.manifest_file = "site.pp"
  	p.module_path = "modules"
  end

end
