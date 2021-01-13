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

### Clean up and reclaim disk space used by docker
https://domm.plix.at/perl/2020_06_docker_prune_volumes_by_label.html

### Create new PostgreSQL container
```bash
docker run --name pgdb -e POSTGRES_PASSWORD=password -e POSTGRES_USER=user -e POSTGRES_DB=dbname -p 0.0.0.0:18731:5432 -d -v `pwd`/bot_pg:/var/lib/postgresql/data postgres
```
This will make your Postgres DB stick out in the open so use a strong password and change port! In this example I've used 18731 port. Feel free to pick any other non-obvious port. As for getting strong password - use https://gerbill.github.io/sha/ and take a good portion of a generated hash there. 30 symbols should be enough.


### Create new Redis container
```bash
docker run -d -p 26379:6379 -v ~/my-redis:/data --name my-redis redis --requirepass 480f69c349f65332f47076099967c --appendonly yes
```
This will create Redis container named `my-redis` and with a volume with persistance AOF in your home directory: `/home/yourusername/my-redis`  
Create strong password at [https://gerbill.github.io/sha/](https://gerbill.github.io/sha/) as your new `my-redis` container will be listening to outside connections on port `26379` (change this to less obvious number in the command above if you like)
