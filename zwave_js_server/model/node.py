"""Provide a model for the Z-Wave JS node."""
from typing import List

from ..event import Event, EventBase
from .device_class import DeviceClass
from .device_config import DeviceConfig
from .value import Value, value_id


class Node(EventBase):
    """Represent a Z-Wave JS node."""

    def __init__(self, data: dict) -> None:
        """Initialize the node."""
        super().__init__()
        self.data = data
        self.values = {value_id(self, val): Value(self, val) for val in data["values"]}

    @property
    def node_id(self) -> int:
        """Return the node_id."""
        return self.data.get("nodeId")

    @property
    def index(self) -> int:
        """Return the index."""
        return self.data.get("index")

    @property
    def installer_icon(self) -> int:
        """Return the installer_icon."""
        return self.data.get("installerIcon")

    @property
    def user_icon(self) -> int:
        """Return the user_icon."""
        return self.data.get("userIcon")

    @property
    def status(self) -> int:
        """Return the status."""
        return self.data.get("status")

    @property
    def ready(self) -> bool:
        """Return the ready."""
        return self.data.get("ready")

    @property
    def device_class(self) -> DeviceClass:
        """Return the device_class."""
        return DeviceClass(self.data.get("deviceClass", {}))

    @property
    def is_listening(self) -> bool:
        """Return the is_listening."""
        return self.data.get("isListening")

    @property
    def is_frequent_listening(self) -> bool:
        """Return the is_frequent_listening."""
        return self.data.get("isFrequentListening")

    @property
    def is_routing(self) -> bool:
        """Return the is_routing."""
        return self.data.get("isRouting")

    @property
    def max_baud_rate(self) -> int:
        """Return the max_baud_rate."""
        return self.data.get("maxBaudRate")

    @property
    def is_secure(self) -> bool:
        """Return the is_secure."""
        return self.data.get("isSecure")

    @property
    def version(self) -> int:
        """Return the version."""
        return self.data.get("version")

    @property
    def is_beaming(self) -> bool:
        """Return the is_beaming."""
        return self.data.get("isBeaming")

    @property
    def manufacturer_id(self) -> int:
        """Return the manufacturer_id."""
        return self.data.get("manufacturerId")

    @property
    def product_id(self) -> int:
        """Return the product_id."""
        return self.data.get("productId")

    @property
    def product_type(self) -> int:
        """Return the product_type."""
        return self.data.get("productType")

    @property
    def firmware_version(self) -> str:
        """Return the firmware_version."""
        return self.data.get("firmwareVersion")

    @property
    def zwave_plus_version(self) -> int:
        """Return the zwave_plus_version."""
        return self.data.get("zwavePlusVersion")

    @property
    def node_type(self) -> int:
        """Return the node_type."""
        return self.data.get("nodeType")

    @property
    def role_type(self) -> int:
        """Return the role_type."""
        return self.data.get("roleType")

    @property
    def name(self) -> str:
        """Return the name."""
        return self.data.get("name")

    @property
    def location(self) -> str:
        """Return the location."""
        return self.data.get("location")

    @property
    def device_config(self) -> DeviceConfig:
        """Return the device_config."""
        return DeviceConfig(self.data.get("deviceConfig", {}))

    @property
    def label(self) -> str:
        """Return the label."""
        return self.data.get("label")

    @property
    def neighbors(self) -> List[int]:
        """Return the neighbors."""
        return self.data.get("neighbors")

    @property
    def endpoint_count_is_dynamic(self) -> bool:
        """Return the endpoint_count_is_dynamic."""
        return self.data.get("endpointCountIsDynamic")

    @property
    def endpoints_have_identical_capabilities(self) -> bool:
        """Return the endpoints_have_identical_capabilities."""
        return self.data.get('"endpointsHaveIdenticalCapabilities')

    @property
    def individual_endpoint_count(self) -> int:
        """Return the individual_endpoint_count."""
        return self.data.get("individualEndpointCount")

    @property
    def aggregated_endpoint_count(self) -> int:
        """Return the aggregated_endpoint_count."""
        return self.data.get("aggregatedEndpointCount")

    @property
    def interview_attempts(self) -> int:
        """Return the interview_attempts."""
        return self.data.get("interviewAttempts")

    def receive_event(self, event: Event) -> None:
        """Receive an event."""
        self._handle_event_protocol(event)
        event.data["node"] = self

        self.emit(event.data["event"], event.data)

    def handle_wake_up(self, event: Event) -> None:
        """Process a node wake up event."""

    def handle_sleep(self, event: Event) -> None:
        """Process a node sleep event."""

    def handle_dead(self, event: Event) -> None:
        """Process a node dead event."""

    def handle_alive(self, event: Event) -> None:
        """Process a node alive event."""

    def handle_interview_completed(self, event: Event) -> None:
        """Process a node interview completed event."""

    def handle_interview_failed(self, event: Event) -> None:
        """Process a node interview failed event."""

    def handle_ready(self, event: Event) -> None:
        """Process a node ready event."""

    def handle_value_added(self, event: Event) -> None:
        """Process a node value added event."""
        value = Value(self, event.data["args"])
        self.values[value.value_id] = event.data["value"] = value

    def handle_value_updated(self, event: Event) -> None:
        """Process a node value updated event."""
        value = self.values.get(value_id(self, event.data["args"]))
        if value is None:
            # TODO decide how to handle value updated for unknown values
            print()
            print("Value updated for unknown value", value_id(self, event.data["args"]))
            print("Available value IDs", ", ".join(self.values))
            print()
            value = Value(self, event.data["args"])
            self.values[value.value_id] = value
        else:
            value.receive_event(event)
        event.data["value"] = value

    def handle_value_removed(self, event: Event) -> None:
        """Process a node value removed event."""
        event.data["value"] = self.values.pop(value_id(self, event.data["args"]))

    def handle_value_notification(self, event: Event) -> None:
        """Process a node value notification event."""

    def handle_metadata_updated(self, event: Event) -> None:
        """Process a node metadata updated event."""

    def handle_notification(self, event: Event) -> None:
        """Process a node notification event."""

    def handle_firmware_update_progress(self, event: Event) -> None:
        """Process a node firmware update progress event."""

    def handle_firmware_update_finished(self, event: Event) -> None:
        """Process a node firmware update finished event."""
