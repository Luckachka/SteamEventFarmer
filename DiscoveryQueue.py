from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class DiscoveryQueue:
    url = "https://store.steampowered.com/explore/"

    def __init__(self, browser):
        self.browser = browser

    def start(self):
        self.browser.get(DiscoveryQueue.url)
        self.wait_for_load()

        first = self.class_name("discovery_queue_overlay_bg")
        second = self.id_name("refresh_queue_btn")

        try:
            first.click()
        except:
            second.click()

        self.do_queue()

    def do_queue(self):
        next_queue = self.class_name("next_in_queue_content")
        while next_queue is not None:
            next_queue.click()
            self.wait_for_load()
            next_queue = self.class_name("next_in_queue_content")
        self.id_name("refresh_queue_btn").click()
        self.wait_for_load(time=3)

    def class_name(self, el):
        try:
            return self.browser.find_element_by_class_name(el)
        except:
            return None

    def id_name(self, el):
        try:
            return self.browser.find_element_by_id(el)
        except:
            return None

    def wait_for_load(self, el="responsive_page", time=1.5):
        try:
            WebDriverWait(self.browser, time).until(
                EC.presence_of_element_located((By.CLASS_NAME, el))
            )
        except:
            WebDriverWait(self.browser, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, el))
            )
