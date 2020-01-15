
class Methods:

    def __init__(self, app):
        self.app = app

    def open_page(self):
        driver = self.app.driver
        driver.get('http://blog.csssr.ru/qa-engineer/')

    def go_to_second_tab(self):
        driver = self.app.driver
        driver.find_element_by_link_text('НАХОДИТЬ НЕСОВЕРШЕНСТВА').click()

    def find_link(self):
        driver = self.app.driver
        actual_link = driver.find_element_by_link_text('Софт для быстрого создания скриншотов')
        link_text = actual_link.get_attribute('href')
        assert link_text == 'http://monosnap.com/', 'The link is wrong!'
