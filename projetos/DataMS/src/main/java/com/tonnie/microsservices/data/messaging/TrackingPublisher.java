package com.tonnie.microsservices.data.messaging;

import com.tonnie.microsservices.data.dto.TrackingDto;
import com.tonnie.microsservices.data.model.Tracking;
import org.springframework.amqp.rabbit.core.RabbitTemplate;
import org.springframework.stereotype.Component;

@Component
public class TrackingPublisher implements ITrackingPublisher {

    private final RabbitTemplate rabbitTemplate;

    public TrackingPublisher(RabbitTemplate rabbitTemplate) {
        this.rabbitTemplate = rabbitTemplate;
    }

    @Override
    public void publishTracking(TrackingDto tracking) {
        rabbitTemplate.convertAndSend("tracking-exchange", "tracking.new", tracking);
    }
}
