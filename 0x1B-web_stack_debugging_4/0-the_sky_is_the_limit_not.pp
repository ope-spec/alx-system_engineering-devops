# Interpreted on Ubuntu 14.04 LTS

# 1. Create a custom file with the desired ULIMIT value
file { '/etc/default/nginx_custom':
  ensure  => file,
  content => "ulimit -n 4096\n",
}

# 2. Copy the custom file over the original Nginx file
exec { 'copy-nginx-custom':
  command => '/bin/cp /etc/default/nginx_custom /etc/default/nginx',
  path    => '/bin',
  require => File['/etc/default/nginx_custom'],
}

# 3. Restart Nginx to apply changes
service { 'nginx':
  ensure  => 'running',
  enable  => true,
  require => Exec['copy-nginx-custom'],
}
