package com.tonnie.microsservices.data.messaging;


import org.springframework.amqp.core.Queue;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

@Configuration
public class RabbitMQConfig {

    public static final String LOCATION_QUEUE = "locationQueue";

    @Value("${spring.rabbitmq.queue-name}")
    private String locationQueueName;


    @Bean(name = LOCATION_QUEUE)
    public Queue locationQueue() {
        return new Queue(locationQueueName, false);
    }
}