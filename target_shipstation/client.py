
from target_hotglue.client import HotglueSink
import base64

class ShipStationSink(HotglueSink):
    """ShipStation target sink class."""

    @property
    def http_headers(self) -> dict:
        """Return the http headers needed."""
        encoded_string = f"{self.config.get('api_key')}:{self.config.get('api_password')}".encode("utf-8")
        token = base64.b64encode(encoded_string).decode("utf-8")
        headers = {
            "Authorization": f"Basic {token}"
        }
        return headers

    base_url = "https://ssapi.shipstation.com"

    def upsert_record(self, record: dict, context: dict):
        method = "POST"

        response = self.request_api(method, request_data=record)
        id = response.json().get("orderId")
        return id, True, dict()
