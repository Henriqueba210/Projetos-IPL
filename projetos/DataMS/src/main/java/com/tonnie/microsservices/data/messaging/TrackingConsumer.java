package com.tonnie.microsservices.data.messaging;

import com.tonnie.microsservices.data.dto.TrackingDto;
import com.tonnie.microsservices.data.exceptions.ItemNotFoundException;
import com.tonnie.microsservices.data.mapper.TrackingMapper;
import com.tonnie.microsservices.data.model.Tracking;
import com.tonnie.microsservices.data.service.TelemetryProfileService;
import com.tonnie.microsservices.data.service.TrackingService;
import com.tonnie.microsservices.data.service.VehicleService;
import lombok.extern.slf4j.Slf4j;
import org.springframework.amqp.rabbit.annotation.RabbitListener;
import org.springframework.stereotype.Component;

import java.text.MessageFormat;

@Component
@Slf4j
public class TrackingConsumer {
    private final TrackingMapper trackingMapper;
    private final TrackingService trackingService;
    private final TelemetryProfileService telemetryProfileService;

    private final VehicleService vehicleService;

    public TrackingConsumer(TrackingMapper trackingMapper, TrackingService trackingService, VehicleService vehicleService, TelemetryProfileService telemetryProfileService) {
        this.trackingMapper = trackingMapper;
        this.trackingService = trackingService;
        this.vehicleService = vehicleService;
        this.telemetryProfileService = telemetryProfileService;
    }

    @RabbitListener(queues = "${spring.rabbitmq.queue-name}")
    public void receiveMessage(TrackingDto trackingDto) {
        try {
            if(!vehicleService.checkIfVehicleExists(trackingDto.getIdVehicle()))
                throw new ItemNotFoundException(MessageFormat.format("Vehicle with id {0} does not exist", trackingDto.getIdVehicle()));
            if(!telemetryProfileService.checkIfTelemetryProfileExists(trackingDto.getIdTelemetryProfile()))
                throw new ItemNotFoundException(MessageFormat.format("Telemetry profile with id {0} does not exist", trackingDto.getIdTelemetryProfile()));

            Tracking tracking = trackingMapper.toEntity(trackingDto);
            trackingService.createTracking(tracking);
        } catch (Exception e) {
            log.error("Error while processing message: " + e.getMessage(), e);
        }
    }
}
