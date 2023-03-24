# this will be used to kill a command called killmenow

exec { 'Kill Script':
  path    => ['/bin', '/sbin'],
  command => 'pkill killmenow'
}
