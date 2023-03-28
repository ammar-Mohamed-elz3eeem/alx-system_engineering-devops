# configure server config
exec { 'update system':
  command => 'apt-get update',
  path    => ['/usr/bin', '/usr/sbin']
}

package { 'nginx':
  ensure  => installed,
  require => Exec["update system"]
}

file { '/var/www/html/index.html':
  content => 'Hello World!'
}

exec { 'redirection page':
  command => 'sed -i "25i\	rewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;" /etc/nginx/sites-enabled/default;',
  path    => ["/usr/sbin", "/usr/bin"]
}

service { 'nginx':
  ensure  => running,
  require => Package['nginx']
}
