package com.tonnie.microsservices.data.service;

import com.tonnie.microsservices.data.model.Tracking;
import com.tonnie.microsservices.data.repository.TrackingRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.Optional;
import java.util.UUID;

@Service
public class TrackingService {

    @Autowired
    private TrackingRepository trackingRepository;

    public Optional<Tracking> getTrackingById(UUID id) {
        return trackingRepository.findById(id);
    }

    public List<Tracking> getAllTrackings() {
        return trackingRepository.findAll();
    }

    public Tracking createTracking(Tracking tracking) {
        return trackingRepository.save(tracking);
    }

    public Tracking updateTracking(Tracking tracking) {
        return trackingRepository.save(tracking);
    }

    public void deleteTracking(UUID id) {
        trackingRepository.deleteById(id);
    }
}
