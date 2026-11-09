import dataclasses

class Request_Handler:
    def __init__(self, request_builder):
        self.request_builder = request_builder

    def handle_request(self, location: str, start_date: str, end_date: str) -> dict:
        request_data = self.request_builder.build_request(location, start_date, end_date)
        return request_data