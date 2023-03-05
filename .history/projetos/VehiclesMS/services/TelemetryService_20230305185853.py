from http import HTTPStatus

from clients.ipl_tracking_microservice_api_client import client
from clients.ipl_tracking_microservice_api_client.api.telemetry_profile import get_telemetry_profile


class TelemetryService:
    client = client.Client(base_url='http://telemetry:8080/tracking')

    def check_if_telemetry_id_is_valid(self, telemetry_id: str) -> bool:
        """
        Check if telemetry ID passed by the user is valid through the Telemetry API
        :type telemetry_id: str
        """
        response = get_telemetry_profile.sync_detailed(telemetry_id, client=self.client)
        return response.status_code == HTTPStatus.OK
