from requests import get

class APIsGuru:
	def __init__(self) -> None:
		self.api = "https://api.apis.guru"
		self.headers = {
			"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36"
		}

	def get_all_apis(self) -> dict:
		return get(
			f"{self.api}/list.json",
			headers=self.headers).json()

	def get_basic_metrics(self) -> dict:
		return get(
			f"{self.api}/metrics.json",
			headers=self.headers).json()
