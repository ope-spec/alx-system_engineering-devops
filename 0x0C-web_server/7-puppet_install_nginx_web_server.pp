# Install Nginx web server (w/ Puppet)

package { 'nginx':
  ensure => 'present',
}

exec { 'install':
  command  => 'sudo apt-get update ; sudo apt-get -y install nginx',
  provider => shell,
}

exec { 'Hello':
  command  => 'echo "Hello World!" | sudo tee /var/www/html/index.html',
  provider => shell,
}

exec { 'configure_redirect':
  command  => 'sudo sed -i "s/listen 80 default_server;/listen 80 default_server;\\n\\tlocation \\/redirect_me {\\n\\t\\treturn 301 https:\\/\\/youtube.com\\/\\watch?v=QH2-TGUlwu4;\\n\\t}/" /etc/nginx/sites-available/default && sudo service nginx restart',
  provider => shell,
}
