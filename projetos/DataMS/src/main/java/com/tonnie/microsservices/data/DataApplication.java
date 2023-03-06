package com.tonnie.microsservices.data;

import com.rabbitmq.client.BuiltinExchangeType;
import com.rabbitmq.client.Channel;
import com.rabbitmq.client.Connection;
import com.rabbitmq.client.ConnectionFactory;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

import java.io.IOException;
import java.util.HashMap;
import java.util.Map;
import java.util.concurrent.TimeoutException;

@SpringBootApplication
public class DataApplication {
	private static final String ORDERS_QUEUE_NAME = "tracking-exchange";
	private static final String ORDERS_EXCHANGE_NAME = "tracking-direct-exchange";
	private static final String ORDERS_ALTERNATE_EXCHANGE_NAME = "tracking-alternate-exchange";
	private static final String ORDERS_ROUTING_KEY = "tracking.new";

	public static void main(String[] args) {
		SpringApplication.run(DataApplication.class, args);
		try{
			declareQueues();
		} catch (Exception e) {
			e.printStackTrace();
		}
	}

	private static void declareQueues() throws IOException, TimeoutException {
		ConnectionFactory factory = new ConnectionFactory();
		factory.setUsername("user");
		factory.setPassword("password");
		factory.setHost("ipl-rabbitmq");
		Connection connection = factory.newConnection();
		Channel channel = connection.createChannel();

		Map<String, Object> exchangeArguments = new HashMap<>();
		exchangeArguments.put("alternate-exchange", ORDERS_ALTERNATE_EXCHANGE_NAME);
		channel.exchangeDeclare(ORDERS_EXCHANGE_NAME, BuiltinExchangeType.DIRECT, true, false, exchangeArguments);

		Map<String, Object> queueArguments = new HashMap<>();
		channel.queueDeclare(ORDERS_QUEUE_NAME, false, false, false, queueArguments);

		channel.queueBind(ORDERS_QUEUE_NAME, ORDERS_EXCHANGE_NAME, ORDERS_ROUTING_KEY);
	}
}
