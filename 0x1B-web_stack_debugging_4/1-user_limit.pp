# enable user holberton to write & exec commands

exec { 'enable hard limit for user holberton':
  command => 'sed -i "/holberton hard/s/5/50000/" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/'
}

exec { 'enable soft limit for user holberton':
  command => 'sed -i "/holberton sodt/s/4/50000/" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/'
}
