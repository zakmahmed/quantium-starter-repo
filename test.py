from app import dash_app


def test_visualization_is_present(dash_duo):
    dash_duo.start_server(dash_app)
    dash_duo.wait_for_element("#visualization", timeout=1)


def test_header_is_present(dash_duo):
    dash_duo.start_server(dash_app)
    dash_duo.wait_for_element("#header", timeout=10)


def test_region_picker_is_present(dash_duo):
    dash_duo.start_server(dash_app)
    dash_duo.wait_for_element("#button", timeout=10)
