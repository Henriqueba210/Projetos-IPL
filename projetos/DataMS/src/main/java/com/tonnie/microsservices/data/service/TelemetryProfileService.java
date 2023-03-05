package com.tonnie.microsservices.data.service;

import com.tonnie.microsservices.ApiClient;
import com.tonnie.microsservices.ApiException;
import com.tonnie.microsservices.Configuration;
import com.tonnie.microsservices.api.TelemetryProfileApi;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.stereotype.Service;

@Service
public class TelemetryProfileService {
    private final TelemetryProfileApi telemetryProfileApi;

    @Value("${clients.telemetry_profile.base_path}")
    private static final String BASE_PATH = "";

    TelemetryProfileService() {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath(BASE_PATH);
        this.telemetryProfileApi = new TelemetryProfileApi(defaultClient);
    }

    public boolean checkIfTelemetryProfileExists(String vehicleId) throws ApiException {
        var vehicleExists = false;
        try {
            var response = telemetryProfileApi.deleteTelemetryProfileWithHttpInfo(vehicleId);
            if (response.getStatusCode() == 200) {
                vehicleExists = true;
            }
        } catch (ApiException e) {
            if (e.getCode() != 404) {
                throw e;
            }
        }
        return vehicleExists;
    }
}