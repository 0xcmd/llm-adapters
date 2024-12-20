from adapters.abstract_adapters.openai_sdk_chat_adapter import OpenAISDKChatAdapter
from adapters.types import Cost, Model, ModelProperties, Provider, Vendor


class AI21Model(Model):
    provider_name: str = Provider.ai21.value
    vendor_name: str = Vendor.ai21.value

    # supports_vision: bool = False
    # supports_tools: bool = False

    properties: ModelProperties = ModelProperties(open_source=True, gdpr_compliant=True)

    def _get_api_path(self) -> str:
        return f"{self.name}"


MODELS: list[Model] = [
    AI21Model(
        name="jamba-1.5-mini",
        cost=Cost(prompt=0.2e-6, completion=0.4e-6),
        context_length=256000,
        supports_only_system=False,
        supports_json_content=False,
        supports_empty_content=False,
        supports_vision=False,
    ),
    AI21Model(
        name="jamba-1.5-large",
        cost=Cost(prompt=2.0e-6, completion=8.0e-6),
        context_length=256000,
        supports_only_system=False,
        supports_json_content=False,
        supports_empty_content=False,
        supports_vision=False,
    ),
]


class AI21SDKChatProviderAdapter(OpenAISDKChatAdapter):
    @staticmethod
    def get_supported_models() -> list[Model]:
        return MODELS

    @staticmethod
    def get_api_key_name() -> str:
        return "AI21_API_KEY"

    def get_base_sdk_url(self) -> str:
        return "https://api.ai21.com/studio/v1"
