# -*- coding: utf-8 -*-

import time
import logging
import pychrome


logging.basicConfig(level=logging.INFO)


def close_all_tabs(browser):
    if len(browser.list_tab()) == 0:
        return

    for tab in browser.list_tab():
        browser.close_tab(tab)

    time.sleep(1)
    assert len(browser.list_tab()) == 0


def setup_function(function):
    browser = pychrome.Browser()
    close_all_tabs(browser)


def teardown_function(function):
    browser = pychrome.Browser()
    close_all_tabs(browser)


def test_chome_version():
    browser = pychrome.Browser()
    browser_version = browser.version()
    assert isinstance(browser_version, dict)


def test_browser_list():
    browser = pychrome.Browser()
    tabs = browser.list_tab()
    assert len(tabs) == 0


def test_browser_new():
    browser = pychrome.Browser()
    browser.new_tab()
    tabs = browser.list_tab()
    assert len(tabs) == 1


def test_browser_activate_tab():
    browser = pychrome.Browser()
    tabs = []
    for i in range(10):
        tabs.append(browser.new_tab())

    for tab in tabs:
        browser.activate_tab(tab)

def test_browser_get_current_tab():
    browser = pychrome.Browser()
    tab1 = browser.new_tab()
    tab2 = browser.new_tab()

    browser.activate_tab(tab1)
    current_tab = browser.get_current_tab()
    assert current_tab == tab1

    browser.activate_tab(tab2)
    current_tab = browser.get_current_tab()
    assert current_tab == tab2

    browser.close_tab(tab2)
    current_tab = browser.get_current_tab()
    assert current_tab == tab1

    browser.close_tab(tab1)
    current_tab = browser.get_current_tab()
    assert current_tab is None

def test_browser_tabs_map():
    browser = pychrome.Browser()

    tab = browser.new_tab()
    assert tab in browser.list_tab()
    assert tab in browser.list_tab()

    browser.close_tab(tab)
    assert tab not in browser.list_tab()


def test_browser_new_10_tabs():
    browser = pychrome.Browser()
    tabs = []
    for i in range(10):
        tabs.append(browser.new_tab())

    time.sleep(1)
    assert len(browser.list_tab()) == 10

    for tab in tabs:
        browser.close_tab(tab.id)

    time.sleep(1)
    assert len(browser.list_tab()) == 0


def test_browser_new_100_tabs():
    browser = pychrome.Browser()
    tabs = []
    for i in range(100):
        tabs.append(browser.new_tab())

    time.sleep(1)
    assert len(browser.list_tab()) == 100

    for tab in tabs:
        browser.close_tab(tab)

    time.sleep(1)
    assert len(browser.list_tab()) == 0
