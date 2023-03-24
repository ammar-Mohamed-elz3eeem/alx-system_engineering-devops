# install flask on our web server

package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3'
}
