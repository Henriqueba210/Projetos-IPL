package com.tonnie.microsservices.data.mapper;

import com.tonnie.microsservices.data.dto.TrackingDto;
import com.tonnie.microsservices.data.model.Tracking;
import org.mapstruct.Mapper;

@Mapper(componentModel = "spring")

public interface TrackingMapper {

    TrackingDto toDto(Tracking tracking);

    Tracking toEntity(TrackingDto trackingDto);
}
