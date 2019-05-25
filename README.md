# RabbitMQ samples

```
docker run -d --hostname localhost --name rabbitmq -p 15672:15672 -p 5672:5672 rabbitmq:3-management
```

- visit http://localhost:15672
- create exchange named "first_exchange"
- create queue named "first_queue"
