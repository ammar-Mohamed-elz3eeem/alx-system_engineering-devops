# fix nginx request limit

exec { 'Fix Nginx':
  command => "sed -i 's/15/4096/' /etc/default/nginx",
  path    => ["/bin", "/usr/local/bin"]
}

service { 'nginx':
  ensure  => running,
  restart => 'pkill -HUP nginx'
}
