package com.tonnie.microsservices.data.controller;

import com.tonnie.microsservices.data.dto.TrackingDto;
import com.tonnie.microsservices.data.mapper.TrackingMapper;
import com.tonnie.microsservices.data.messaging.ITrackingPublisher;
import com.tonnie.microsservices.data.model.Tracking;
import com.tonnie.microsservices.data.service.TrackingService;
import jakarta.validation.Valid;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;
import java.util.Optional;
import java.util.UUID;

@RestController
@RequestMapping("/api/trackings")
public class TrackingController {

    private final TrackingService trackingService;
    protected final TrackingMapper trackingMapper;
    protected final ITrackingPublisher trackingPublisher;

    public TrackingController(TrackingService trackingService, TrackingMapper trackingMapper, ITrackingPublisher trackingPublisher) {
        this.trackingService = trackingService;
        this.trackingMapper = trackingMapper;
        this.trackingPublisher = trackingPublisher;
    }
    
    @GetMapping("/{id}")
    public ResponseEntity<TrackingDto> getTrackingById(@PathVariable("id") UUID id) {
        Optional<Tracking> tracking = trackingService.getTrackingById(id);
        return tracking.map(value -> ResponseEntity.ok(trackingMapper.toDto(value))).orElseGet(() -> ResponseEntity.notFound().build());
    }

    @GetMapping("/vehicle/{vehicleId}/tracking")
    public ResponseEntity<List<TrackingDto>> getVehicleTracking(@PathVariable("vehicleId") String vehicleId) {
        List<TrackingDto> trackingDTOs = trackingService.getTrackingByVehicleId(vehicleId).stream().map(trackingMapper::toDto).toList();
        return ResponseEntity.ok(trackingDTOs);
    }

    @GetMapping("/telemetry-profile/{idTelemetryProfile}")
    public ResponseEntity<List<TrackingDto>> getTrackingByTelemetryProfile(@PathVariable String idTelemetryProfile) {
        List<TrackingDto> trackings = trackingService.getTrackingByTelemetryProfileId(idTelemetryProfile).stream().map(trackingMapper::toDto).toList();
        return ResponseEntity.ok(trackings);
    }

    @GetMapping
    public ResponseEntity<List<TrackingDto>> getAllTrackings() {
        List<Tracking> trackings = trackingService.getAllTrackings();
        List<TrackingDto> trackingDtos = trackings.stream().map(trackingMapper::toDto).toList();
        return ResponseEntity.ok(trackingDtos);
    }

    @PostMapping
    @ResponseStatus(HttpStatus.CREATED)
    public void createTracking(@RequestBody @Valid TrackingDto trackingDto) {
        trackingPublisher.publishTracking(trackingDto); // publish the tracking entity
    }
}
