CREATE TABLE tracking (
                          id UUID PRIMARY KEY,
                          id_vehicle VARCHAR(255) NOT NULL,
                          id_telemetry_profile VARCHAR(255) NOT NULL,
                          date TIMESTAMP NOT NULL,
                          latitude VARCHAR(255) NOT NULL,
                          longitude VARCHAR(255) NOT NULL
);