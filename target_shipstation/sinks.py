"""ShipStation target sink class, which handles writing streams."""


from target_shipstation.client import ShipStationSink

class FallbackSink(ShipStationSink):
    """ShipStation target sink class."""

    @property
    def name(self) -> str:
        return self.stream_name

    @property
    def endpoint(self) -> str:
        if self.stream_name == "orders":
            return "/orders/createorder"

        return f"/{self.stream_name}"

    def preprocess_record(self, record: dict, context: dict) -> None:
        """Process the record."""
        return record
