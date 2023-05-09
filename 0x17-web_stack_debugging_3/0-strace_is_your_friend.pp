# command to fix wordpress issue in apache server

exec {'remove bad extension':
  command => "sed -i 's/phpp/php/g' /var/www/html/wp-settings.php",
  path    => ["/usr/local/bin/","/bin/"]
}
