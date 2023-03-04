package com.tonnie.microsservices.data.messaging;

import com.tonnie.microsservices.data.dto.TrackingDto;
import com.tonnie.microsservices.data.mapper.TrackingMapper;
import com.tonnie.microsservices.data.model.Tracking;
import com.tonnie.microsservices.data.service.TrackingService;
import org.springframework.amqp.rabbit.annotation.RabbitListener;
import org.springframework.stereotype.Component;

@Component
public class TrackingConsumer {
    private final TrackingMapper trackingMapper;
    private final TrackingService trackingService;


    public TrackingConsumer(TrackingMapper trackingMapper, TrackingService trackingService) {
        this.trackingMapper = trackingMapper;
        this.trackingService = trackingService;
    }

    @RabbitListener(queues = "${spring.rabbitmq.queue-name}")
    public void receiveMessage(TrackingDto trackingDto) {
        Tracking tracking = trackingMapper.toEntity(trackingDto);
        trackingService.createTracking(tracking);
    }
}
