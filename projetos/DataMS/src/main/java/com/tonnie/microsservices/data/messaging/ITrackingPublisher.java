package com.tonnie.microsservices.data.messaging;

import com.tonnie.microsservices.data.dto.TrackingDto;

public interface ITrackingPublisher {
    void publishTracking(TrackingDto tracking);
}