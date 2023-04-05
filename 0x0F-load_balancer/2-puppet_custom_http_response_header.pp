# - setup New Ubuntu server with nginx
# - add a custom HTTP header

exec { 'update system':
  command => '/usr/bin/apt-get update'
}

package { 'nginx':
  ensure  => 'installed',
  require => Exec['update system']
}

file { '/var/www/html/index.html':
  content => 'Hello World!'
}

exec { 'redirect_me command':
  command  => 'sed -i "24i\    rewrite ^/redirect_me$ https://www.youtube.com/ permanent;" /etc/nginx/sites-available/default',
  provider => 'shell'
}

exec { 'add header':
  command  => 'sed -i "25i\    add_header X-Served-By \$hostname;" /etc/nginx/sites-available/default',
  provider => 'shell'
}

service { 'nginx':
  ensure  => running,
  require => Package['nginx']
}
