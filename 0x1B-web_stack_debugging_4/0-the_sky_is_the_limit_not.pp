# increases the amount of traffic an Nginx can recieve.

# fix nginx request limit
exec { 'fix: for nginx':
  command => 'sed -i "s/15/4096/" /etc/default/nginx',
  path    => '/usr/local/bin/:/bin/'
} ->

# Restart Nginx
exec { 'restart: nginx-restart':
  command => 'nginx restart',
  path    => '/etc/init.d/'
}
