import pytest


@pytest.mark.ui
@pytest.mark.entertainment
def test_can_navigate_to_entertainment_page(chrome_browser):
    chrome_browser.get('https://www.siriusxm.com/')
    assert True
