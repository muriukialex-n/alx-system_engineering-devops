fest to optimize Nginx configuration for high concurrency

# Increase the ULIMIT for Nginx connections
exec { 'increase-nginx-ulimit':
  command => 'sed -i "s/15/4096/" /etc/default/nginx && service nginx restart',
  path    => '/usr/bin:/bin',
}

# Configure Nginx to handle high concurrency
file { '/etc/nginx/nginx.conf':
  ensure  => file,
  content => '
    worker_processes auto;
    worker_connections 2000;
    events {
      multi_accept on;
      use epoll;
    }
  ',
  notify  => Exec['nginx-restart'],
}

# Restart Nginx
exec { 'nginx-restart':
  command => 'service nginx restart',
  path    => '/etc/init.d/',
  refreshonly => true,
}

# Display a notice about the changes
notify { 'nginx-optimization-notice':
  message => 'Nginx configuration optimized for high concurrency.',
}

