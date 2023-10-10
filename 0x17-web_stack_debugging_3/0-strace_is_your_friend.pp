# replaces occurrences of "phpp" with "php" in the wp-settings.php file.

exec { 'replace_php_with_phpp':
  command => 'sed -i "s/phpp/php/g" /var/www/html/wp-settings.php',
  path    => '/bin:/usr/bin',
  onlyif  => 'test -f /var/www/html/wp-settings.php',
}
