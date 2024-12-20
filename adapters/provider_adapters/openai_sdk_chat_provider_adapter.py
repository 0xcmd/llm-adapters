from adapters.abstract_adapters.openai_sdk_chat_adapter import OpenAISDKChatAdapter
from adapters.types import Cost, Model, ModelProperties, Provider, Vendor


class OpenAIModel(Model):
    provider_name: str = Provider.openai.value
    vendor_name: str = Vendor.openai.value

    properties: ModelProperties = ModelProperties(gdpr_compliant=True)


MODELS: list[Model] = [
    OpenAIModel(
        name="gpt-3.5-turbo",
        cost=Cost(prompt=3.0e-6, completion=6.0e-6),
        context_length=16385,
        completion_length=16385,
        supports_vision=False,
    ),
    OpenAIModel(
        name="gpt-4",
        cost=Cost(prompt=30.0e-6, completion=60.0e-6),
        context_length=8192,
        completion_length=8192,
        supports_json_output=False,
        supports_vision=False,
    ),
    OpenAIModel(
        name="gpt-4-turbo",
        cost=Cost(prompt=10.0e-6, completion=30.0e-6),
        context_length=128000,
        completion_length=4096,
    ),
    OpenAIModel(
        name="gpt-4o",
        cost=Cost(prompt=2.5e-6, completion=10.0e-6),
        context_length=128000,
        completion_length=16384,
    ),
    OpenAIModel(
        name="gpt-4o-2024-05-13",
        cost=Cost(prompt=5.0e-6, completion=15.0e-6),
        context_length=128000,
        completion_length=4096,
    ),
    OpenAIModel(
        name="gpt-4o-2024-08-06",
        cost=Cost(prompt=2.5e-6, completion=10.0e-6),
        context_length=128000,
        completion_length=16384,
    ),
    OpenAIModel(
        name="gpt-4o-mini",
        cost=Cost(prompt=0.15e-6, completion=0.6e-6),
        context_length=128000,
        completion_length=16385,
    ),
    OpenAIModel(
        name="gpt-4o-mini-2024-07-18",
        cost=Cost(prompt=0.15e-6, completion=0.6e-6),
        context_length=128000,
        completion_length=16385,
    ),
    OpenAIModel(
        name="o1-preview",
        cost=Cost(prompt=15.0e-6, completion=60.0e-6),
        context_length=128000,
        completion_length=32768,
        supports_tools=False,
        supports_temperature=False,
        supports_streaming=False,
        supports_system=False,
        supports_n=False,
        supports_vision=False,
        supports_json_output=False,
    ),
    OpenAIModel(
        name="o1-preview-2024-09-12",
        cost=Cost(prompt=15.0e-6, completion=60.0e-6),
        context_length=128000,
        completion_length=32768,
        supports_tools=False,
        supports_temperature=False,
        supports_system=False,
        supports_streaming=False,
        supports_n=False,
        supports_vision=False,
        supports_json_output=False,
    ),
    OpenAIModel(
        name="o1-mini",
        cost=Cost(prompt=3.0e-6, completion=12.0e-6),
        context_length=128000,
        completion_length=65536,
        supports_tools=False,
        supports_temperature=False,
        supports_system=False,
        supports_streaming=False,
        supports_n=False,
        supports_vision=False,
        supports_json_output=False,
    ),
    OpenAIModel(
        name="o1-mini-2024-09-12",
        cost=Cost(prompt=3.0e-6, completion=12.0e-6),
        context_length=128000,
        completion_length=65536,
        supports_tools=False,
        supports_temperature=False,
        supports_system=False,
        supports_streaming=False,
        supports_n=False,
        supports_vision=False,
        supports_json_output=False,
    ),
]


class OpenAISDKChatProviderAdapter(OpenAISDKChatAdapter):
    @staticmethod
    def get_supported_models() -> list[Model]:
        return MODELS

    @staticmethod
    def get_api_key_name() -> str:
        return "OPENAI_API_KEY"

    def get_base_sdk_url(self) -> str:
        return "https://api.openai.com/v1"
