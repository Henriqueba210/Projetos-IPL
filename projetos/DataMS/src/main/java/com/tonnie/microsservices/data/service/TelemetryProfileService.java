package com.tonnie.microsservices.data.service;

import com.tonnie.microsservices.ApiClient;
import com.tonnie.microsservices.ApiException;
import com.tonnie.microsservices.Configuration;
import com.tonnie.microsservices.api.TelemetryProfileApi;
import jakarta.annotation.PostConstruct;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.stereotype.Service;

@Service
public class TelemetryProfileService {
    private TelemetryProfileApi telemetryProfileApi;

    @Value("${clients.telemetry_profile.base_path}")
    private String base_path;

    @PostConstruct
    void init() {
        ApiClient defaultClient = Configuration.getDefaultApiClient();
        defaultClient.setBasePath(base_path);
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