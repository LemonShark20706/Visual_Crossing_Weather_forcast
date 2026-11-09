import dataclasses

@dataclasses.dataclass
class Request_Builder:
    loaded_env_vars: object

    def __init__(self, loaded_env_vars):
        self.loaded_env_vars = loaded_env_vars

    def build_request(self, location: str, start_date: str, end_date: str) -> dict:
        api_key = self.loaded_env_vars.api_key
        base_url = self.loaded_env_vars.base_url

        request_data = {
            "url": f"{base_url}/forecast",
            "params": {
                "location": location,
                "start_date": start_date,
                "end_date": end_date,
                "api_key": api_key
            }
        }

        return request_data