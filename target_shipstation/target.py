"""ShipStation target class."""

from typing import Type
from target_hotglue.target import TargetHotglue
from singer_sdk import typing as th
from singer_sdk.sinks import Sink

from target_shipstation.sinks import (
    FallbackSink,
)

class TargetShipStation(TargetHotglue):
    """Sample target for ShipStation."""

    name = "target-shipstation"
    SINK_TYPES = [FallbackSink]
    config_jsonschema = th.PropertiesList(
        th.Property(
            "api_key",
            th.StringType,
            required=True,
        ),
        th.Property(
            "api_password",
            th.StringType,
            required=True,
        ),
    ).to_dict()

    def get_sink_class(self, stream_name: str) -> Type[Sink]:
        """Always return FallbackSink for any stream (dynamic routing)."""
        return FallbackSink

if __name__ == "__main__":
    TargetShipStation.cli()