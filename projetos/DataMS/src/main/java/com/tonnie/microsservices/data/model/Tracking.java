package com.tonnie.microsservices.data.model;

import jakarta.persistence.*;
import jakarta.validation.constraints.NotNull;
import lombok.*;
import org.hibernate.Hibernate;

import java.util.Date;
import java.util.Objects;
import java.util.UUID;

@Data
@Entity
@Table(name = "tracking")
public class Tracking {
    @Id
    @GeneratedValue(strategy = GenerationType.UUID)
    private UUID id;

    @NotNull
    private String idVehicle;

    @NotNull
    private String idTelemetryProfile;

    @Temporal(TemporalType.TIMESTAMP)
    @NotNull
    private Date date;

    @NotNull
    private String latitude;

    @NotNull
    private String longitude;
}
