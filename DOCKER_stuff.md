# Docker Stuff
Some useful docker things to remember...

### Nginx-Proxy
Taken from https://blog.ssdnodes.com/blog/host-multiple-websites-docker-nginx/  
Create a Docker network
```bash
docker network create nginx-proxy
```
Install nginx-proxy container
```bash
docker run -d -p 80:80 --name nginx-proxy --net nginx-proxy -v /var/run/docker.sock:/tmp/docker.sock jwilder/nginx-proxy
```
As an example: start a WordPress container with a basic configuration
```bash
docker run -d --name blog --expose 80 --net nginx-proxy -e VIRTUAL_HOST=blog.DOMAIN.TLD wordpress
```
More info on https://github.com/nginx-proxy/nginx-proxy  
For HTTPS check https://github.com/nginx-proxy/docker-letsencrypt-nginx-proxy-companion
