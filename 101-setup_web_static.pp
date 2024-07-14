#Install nginx if not already installed
package {'nginx':
    ensure => installed,
}

#Create /data/ directory
file {'/data/':

    ensure  => directory,
    owner   => 'ubuntu',
    group   => 'ubuntu',
    recurse => 'true',
}

#Create /web_static/ directory
file {'/data/web_static/':

    ensure => directory,
    owner => 'ubuntu',
    group => 'ubuntu',
    recurse => 'true',

}

#Create /releases/ directory
file {'/data/web_static/releases/':

    ensure => directory,
    owner => 'ubuntu',
    group => 'ubuntu',
    recurse => 'true',

}

#Create /shared/ directory
file {'/data/web_static/shared/':

    ensure => directory,
    owner => 'ubuntu',
    group => 'ubuntu',
    recurse => 'true',

}

#Create /test/ directory
file {'/data/web_static/releases/test/':

    ensure => directory,
    owner => 'ubuntu',
    group => 'ubuntu',
    recurse => 'true',

}

#Create a tets html file
file {'/data/web_static/releases/test/index.html':

ensure => file,
content => '<html><head></head><body>Holberton School</body></html>',
owner => 'ubuntu',
group => 'ubuntu',

}

#Create a symbolc link to the test directory
file {'/data/web_static/current':

ensure => link,
target => '/data/web_static/releases/test/',
owner => 'ubuntu',
group => 'ubuntu',
force => true,

}

#Create a config file for hbnb_static
file {'/etc/nginx/sites-available/hbnb_static':

ensure => file,
content => @("EOF"),
server {
    listen 80;
    listen [::]:80;

    server_name cityspaces.tech www.cityspaces.tech 100.26.247.135 18.235.248.212;

    location /hbnb_static {
        alias /data/web_static/current;
    }

    location / {
        return 404;
    }
}

server {
    listen 80;
    listen [::]:80;

    server_name localhost;

    location /hbnb_static {
        alias /data/web_static/current;
    }

    location / {
        return 404;
    }
}
EOF
notify => Service['nginx'],

}

#Create a symbolic link to hbnb_static config to activate
file {'/etc/nginx/sites-enabled/hbnb_static':

ensure => link,
target => '/etc/nginx/sites-available/hbnb_static',

}

#Ensure and nginx is running and restarts if the config file changes
service {'nginx':

ensure => running,
enable => true,
subscribe => File['/etc/nginx/sites-available/hbnb_static']

}
