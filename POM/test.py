import pytest
from pages.yandexSearch.init import YandexSearcher
import time

def test_search():
    yandex_page = YandexSearcher()
    yandex_page.go_to_site()
    yandex_page.enter_word("cat")
    yandex_page.click_on_the_search_button()
    time.sleep(2)
    yandex_page.quit_from_browser()
def test_enter_in_field_and_clear_words():
    yandex_page = YandexSearcher()
    yandex_page.go_to_site()
    yandex_page.enter_word("cat")
    yandex_page.click_on_cancel_button()
    yandex_page.enter_word("dog")
    yandex_page.click_on_the_search_button()
    time.sleep(2)
    yandex_page.quit_from_browser()
