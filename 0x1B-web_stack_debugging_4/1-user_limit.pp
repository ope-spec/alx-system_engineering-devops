# Create the holberton user
user { 'holberton':
  ensure     => present,
  managehome => true,
  password   => '$1$CH5ot/l8$dCIO2dXiTykaALvhO.gV91',
}

# Set resource limits for the holberton user
file { '/etc/security/limits.d/holberton.conf':
  ensure  => present,
  content => "holberton hard nofile 50000\nholberton soft nofile 50000\n",
}

exec { 'reload-sysctl':
  command     => '/sbin/sysctl -p',
  path        => '/usr/local/bin:/bin/',
  refreshonly => true,
}

# Enable the session files for the user
file { '/etc/pam.d/common-session':
  content => 'session required pam_limits.so',
}

exec { 'reload-pam':
  command     => 'pam-auth-update',
  path        => '/usr/local/bin:/bin/',
  refreshonly => true,
}
