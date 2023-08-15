# let the user 'holberton' make any requests to 
# open hard & soft files without errors

exec {'enable for hard file':
  command => 'sed -i "/holberton hard/s/5/50000/" /etc/security/limit.conf',
  path    => '/usr/local/bin/:/bin/'
}

exec {'enable for soft file':
  command => 'sed -i "/holberton soft/s/4/50000/" /etc/security/limit.conf',
  path    => '/usr/local/bin/:/bin/'
}
