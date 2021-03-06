# global scope and variables.
$user = "vagrant"

Exec {
	path => [ "/bin", "/sbin", "/usr/bin", "/usr/sbin", "/usr/local/bin", "/usr/local/sbin"],
    user => $user,  timeout => 3600,
   # logoutput => true,
}

# apt-get update for the system
exec { "update":
	  command => "sudo apt-get update",
}

Package { ensure => "installed", require => Exec["update"] }

include bootstrap
include elasticsearch
include rabbitmq
include redis
include postgresql
include python
include nodejs
