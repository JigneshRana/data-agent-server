# data-agent
A data agent is a client-server application based on Python 3 that can exchange data across sockets. By this application, we are only aiming to receive data from the client (remote host) and store it on the server (destination host) for further use.

## data-agent-client
The data-agent client is architected to collect various required data matrics from the linux based webapplication's remote machine. which can be further very useful to see the trend of the web application and what's going on inside the server. 

### For example,
- It collects access request counts, according to its status, for a given time period, which helps to monitor traffic on each server.
- It collects requests counts which are consuming more than 100 seconds, for a given time period.
- It collects the number of warning errors, and notices for a given time period. 
- Not only this, but it can also execute custom commands on the Linux server, based on your config settings.

### Which can helps in the following ways.
- Monitor to see if the critical services are up and running.
- webservers like Apache or Nginx ideal requests workloads on web servers.