import requests

class PlanningCoursesAPI:
    def __init__(self, base_url):
        self.base_url = base_url.rstrip('/')
        self.base_endpoint = f"{self.base_url}/planning/planningcourses"

    def get_courses_by_code(self, code):
        params = {'code': code}
        return self._make_request(self.base_endpoint, params)

    def get_course_by_id(self, course_id):
        endpoint = f"{self.base_endpoint}/{course_id}"
        return self._make_request(endpoint)

    def get_all_courses(self):
        return self._make_request(self.base_endpoint)

    def _make_request(self, endpoint, params=None):
        try:
            response = requests.get(endpoint, params=params)
            response.raise_for_status()  # Raise an exception for HTTP errors
            return response.json()
        except requests.exceptions.RequestException as e:
            # Handle exceptions
            print(f"Error: {e}")
            return None