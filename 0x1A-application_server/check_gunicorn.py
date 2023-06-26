server {
        listen 80 default_server;
        listen [::]:80 default_server;

        root /var/www/html;
        server_name _;

        add_header X-Served-By $hostname;
        
        location /airbnb-onepage {
		proxy-pass http://0.0.0.0:5000/airbnb-onepage
	}

        location / {
                # First attempt to serve request as file, then
                # as directory, then fall back to displaying a 404.
                try_files $uri $uri/ =404;
        }

        rewrite ^/redirect_me$ https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;

        error_page 404 /error_404.html;

        location = /error_404.html {
                internal;
        }
}