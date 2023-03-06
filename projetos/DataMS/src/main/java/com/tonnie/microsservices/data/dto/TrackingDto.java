package com.tonnie.microsservices.data.dto;

import com.tonnie.microsservices.data.model.Tracking;
import lombok.Getter;
import lombok.Setter;
import lombok.ToString;

import java.io.Serializable;
import java.util.Date;
import java.util.UUID;

@Getter
@Setter
@ToString
public class TrackingDto implements Serializable {
    private UUID id;
    private String idVehicle;
    private String idTelemetryProfile;
    private Date date;
    private String latitude;
    private String longitude;
}
