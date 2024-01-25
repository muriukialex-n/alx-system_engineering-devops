exec { 'increase-nginx-connections':
  command => 'sed -i "s/15/4096/" /etc/default/nginx && service nginx restart',
  path    => '/usr/bin:/bin',
}
