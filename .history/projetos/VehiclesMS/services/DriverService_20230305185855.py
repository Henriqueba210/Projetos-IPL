from http import HTTPStatus

from clients.ipl_tracking_microservice_api_client import client
from clients.ipl_tracking_microservice_api_client.api.driver import get_driver


class DriverService:
    client = client.Client(base_url='http://people:8080/tracking')

    def check_if_driver_id_is_valid(self, driver_id: str) -> bool:
        """
        Check if telemetry ID passed by the user is valid through the Telemetry API
        :type driver_id: str
        """
        response = get_driver.sync_detailed(driver_id, client=self.client)
        return response.status_code == HTTPStatus.OK
