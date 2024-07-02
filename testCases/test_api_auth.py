import pytest, allure
import requests
from requests.auth import HTTPBasicAuth, HTTPDigestAuth

url = 'https://httpbin.org/digest-auth/auth/123/123/MD5'
auth = HTTPDigestAuth('123', '123')

@pytest.mark.api
@allure.title('Testing basic authentication')
def test_basicAuth():
    # use the 'auth' parameter to send requests with HTTP Basic Auth:
    headers = {'Accept': 'application/json'}
    r = requests.get(url, auth=auth, verify=False)
    print(r.status_code)
