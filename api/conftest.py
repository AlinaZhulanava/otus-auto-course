def pytest_addoption(parser):
    parser.addoption("--url", action="store", default="https://ya.ru", help="url for test")
    parser.addoption("--status_code", action="store", default="200", help="expected status for the response")
