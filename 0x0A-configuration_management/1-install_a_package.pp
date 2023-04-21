Using Puppet to install flask from pip3
##!/usr/bin/pup

package {'flask':
  ensure   => '2.1.0',
  provider => 'pip',
}
