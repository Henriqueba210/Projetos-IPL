package com.tonnie.microsservices.data.repository;

import com.tonnie.microsservices.data.model.Tracking;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import java.util.List;
import java.util.UUID;

@Repository
public interface TrackingRepository extends JpaRepository<Tracking, UUID> {
    List<Tracking> findByIdVehicle(String idVehicle);

    List<Tracking> findByIdTelemetryProfile(String idTelemetryProfile);
}
