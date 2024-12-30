import pytest


@pytest.fixture()
def dataload():
    print("validate search functionality on the Selenium Playground website")
    return ["Navigates to the Selenium Playground Table Search Demo", "Locates and interacts with the search box to search for New York", "Validates that the search results show 5 entries out of 24 total entries"]


@pytest.fixture(params=["chrome","Navigates to the Selenium Playground Table Search Demo","Locates and interacts with the search box to search for New York","Validates that the search results show 5 entries out of 24 total entries"])
def crossBrowser(request):
    return request.param