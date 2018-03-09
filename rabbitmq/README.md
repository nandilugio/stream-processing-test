
# Run RabbitMQ image
docker run -d --hostname rabbithost --name rabbit -p 15672:15672 -p 5672:5672 rabbitmq:3-management

xdg-open http://localhost:15672
