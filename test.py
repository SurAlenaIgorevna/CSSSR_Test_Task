from application import Application


def test_link(app: Application):
    driver = app.driver

    app.Methods.open_page()
    app.Methods.go_to_second_tab()
    app.Methods.find_link()
