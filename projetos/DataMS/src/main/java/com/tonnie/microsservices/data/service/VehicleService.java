package com.tonnie.microsservices.data.service;

import com.tonnie.microsservices.ApiClient;
import com.tonnie.microsservices.ApiException;
import com.tonnie.microsservices.Configuration;
import com.tonnie.microsservices.api.VehiclesApi;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.stereotype.Service;

import java.util.UUID;

@Service
public class VehicleService {
    private final VehiclesApi vehicleAPI;

    @Value("${clients.vehicles.base_path}")
    private static final String BASE_PATH = "";

    VehicleService() {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath(BASE_PATH);
        this.vehicleAPI = new VehiclesApi(defaultClient);
    }

    public boolean checkIfVehicleExists(String vehicleId) throws ApiException {
        UUID vehicleUUID = UUID.fromString(vehicleId);
        var vehicleExists = false;
        try {
            var vehicle = vehicleAPI.vehiclesVehicleIdGetWithHttpInfo(vehicleUUID);
            if(vehicle.getStatusCode() == 200) {
                vehicleExists = true;
            }
        } catch (ApiException e) {
            if(e.getCode() != 404) {
                throw e;
            }
        }
        return vehicleExists;
    }
}
