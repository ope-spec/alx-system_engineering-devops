# Enhancing Nginx Server Capacity

# 1. Create a custom file with the desired ULIMIT value
file { '/etc/default/nginx_custom':
  content => 'ulimit -n 4096',
} ->

# 2. Copy the custom file over the original Nginx file
exec { 'copy-nginx-custom':
  command => '/usr/bin/sudo cp /etc/default/nginx_custom ' +
             '/etc/default/nginx',
  path    => '/usr/bin:/bin',
} ->

# 3. Restart Nginx to apply changes
exec { 'restart-nginx':
  command => '/usr/bin/sudo service nginx restart',
  path    => '/etc/init.d/',
}
