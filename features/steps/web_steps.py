######################################################################
# Copyright 2016, 2021 John J. Rofrano. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
######################################################################

# pylint: disable=function-redefined, missing-function-docstring
# flake8: noqa
"""
Web Steps

Steps file for web interactions with Selenium

For information on Waiting until elements are present in the HTML see:
    https://selenium-python.readthedocs.io/waits.html
"""
import logging
from behave import when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions

ID_PREFIX = 'product_'


@when('I visit the "Home Page"')
def step_impl(context):
    """ Make a call to the base URL """
    context.driver.get(context.base_url)
    #Uncomment next line to take a screenshot of the web page
    context.driver.save_screenshot('home_page.png')

@then('I should see "{message}" in the title')
def step_impl(context, message):
    """ Check the document title for a message """
    assert(message in context.driver.title)

@then('I should not see "{text_string}"')
def step_impl(context, text_string):
    element = context.driver.find_element(By.TAG_NAME, 'body')
    assert(text_string not in element.text)

@when('I set the "{element_name}" to "{text_string}"')
def step_impl(context, element_name, text_string):
    element_id = ID_PREFIX + element_name.lower().replace(' ', '_')
    element = context.driver.find_element(By.ID, element_id)
    element.clear()
    element.send_keys(text_string)

@when('I select "{text}" in the "{element_name}" dropdown')
def step_impl(context, text, element_name):
    element_id = ID_PREFIX + element_name.lower().replace(' ', '_')
    element = Select(context.driver.find_element(By.ID, element_id))
    element.select_by_visible_text(text)

@then('I should see "{text}" in the "{element_name}" dropdown')
def step_impl(context, text, element_name):
    element_id = ID_PREFIX + element_name.lower().replace(' ', '_')
    element = Select(context.driver.find_element(By.ID, element_id))
    assert(element.first_selected_option.text == text)

@then('the "{element_name}" field should be empty')
def step_impl(context, element_name):
    element_id = ID_PREFIX + element_name.lower().replace(' ', '_')
    element = context.driver.find_element(By.ID, element_id)
    assert(element.get_attribute('value') == u'')

##################################################################
# These two function simulate copy and paste
##################################################################
@when('I copy the "{element_name}" field')
def step_impl(context, element_name):
    element_id = ID_PREFIX + element_name.lower().replace(' ', '_')
    element = WebDriverWait(context.driver, context.wait_seconds).until(
        expected_conditions.presence_of_element_located((By.ID, element_id))
    )
    context.clipboard = element.get_attribute('value')
    logging.info('Clipboard contains: %s', context.clipboard)

@when('I paste the "{element_name}" field')
def step_impl(context, element_name):
    element_id = ID_PREFIX + element_name.lower().replace(' ', '_')
    element = WebDriverWait(context.driver, context.wait_seconds).until(
        expected_conditions.presence_of_element_located((By.ID, element_id))
    )
    element.clear()
    element.send_keys(context.clipboard)

##################################################################
# This code works because of the following naming convention:
# The buttons have an id in the html hat is the button text
# in lowercase followed by '-btn' so the Clean button has an id of
# id='clear-btn'. That allows us to lowercase the name and add '-btn'
# to get the element id of any button
##################################################################

## UPDATE CODE HERE 
@when('I press the "{button}" button')
def step_impl(context, button):
    button_id = button.lower() + '-btn'
    context.driver.find_element_by_id(button_id).click()

@then('I should see "{name}" in the results')
def step_impl(context, name):
    found = WebDriverWait(context.driver, context.wait_seconds).until(
        expected_conditions.text_to_be_present_in_element(
            (By.ID, 'search_results'),
            name
        )
    )
    assert(found)

@then('I should not see "{name}" in the results')
def step_impl(context, name):
    element = context.driver.find_element_by_id('search_results')
    assert(name not in element.text)

@then('I should see the message "{message}"')
def step_impl(context, message):
    found = WebDriverWait(context.driver, context.wait_seconds).until(
        expected_conditions.text_to_be_present_in_element(
            (By.ID, 'flash_message'),
            message
        )
    )
    assert(found)

##################################################################
# This code works because of the following naming convention:
# The id field for text input in the html is the element name
# prefixed by ID_PREFIX so the Name field has an id='pet_name'
# We can then lowercase the name and prefix with pet_ to get the id
##################################################################

@then('I should see "{text_string}" in the "{element_name}" field')
def step_impl(context, text_string, element_name):
    element_id = ID_PREFIX + element_name.lower().replace(' ', '_')
    found = WebDriverWait(context.driver, context.wait_seconds).until(
        expected_conditions.text_to_be_present_in_element_value(
            (By.ID, element_id),
            text_string
        )
    )
    assert(found)

@when('I change "{element_name}" to "{text_string}"')
def step_impl(context, element_name, text_string):
    element_id = ID_PREFIX + element_name.lower().replace(' ', '_')
    element = WebDriverWait(context.driver, context.wait_seconds).until(
        expected_conditions.presence_of_element_located((By.ID, element_id))
    )
    element.clear()
    element.send_keys(text_string)

#Scenario the server is Running

#Scenario Read a product
@when(u'I visit the "Home Page"')
def step_impl(context):
    context.browser.get(f'{context.base_url}/')  # Assuming the home page is the base URL


@when(u'I set the "Name" to "{name}"')
def step_impl(context, name):
    name_field = context.browser.find_element(By.ID, 'name')  # Assuming the ID for the name field
    name_field.send_keys(name)


@when(u'I press the "Search" button')
def step_impl(context):
    search_button = context.browser.find_element(By.XPATH, '//button[contains(text(), "Search")]')
    search_button.click()


@then(u'I should see the message "Success"')
def step_impl(context):
    message = context.browser.find_element(By.ID, 'message')  # Assuming there's an ID for the message element
    assert 'Success' in message.text


@when(u'I copy the "Id" field')
def step_impl(context):
    id_field = context.browser.find_element(By.ID, 'id')  # Assuming the ID of the product field
    context.copied_id = id_field.get_attribute('value')


@when(u'I press the "Clear" button')
def step_impl(context):
    clear_button = context.browser.find_element(By.XPATH, '//button[contains(text(), "Clear")]')
    clear_button.click()


@when(u'I paste the "Id" field')
def step_impl(context):
    id_field = context.browser.find_element(By.ID, 'id')  # Assuming an ID field exists to paste the ID
    id_field.send_keys(context.copied_id)


@when(u'I press the "Retrieve" button')
def step_impl(context):
    retrieve_button = context.browser.find_element(By.XPATH, '//button[contains(text(), "Retrieve")]')
    retrieve_button.click()


@then(u'I should see the message "Success"')
def step_impl(context):
    message = context.browser.find_element(By.ID, 'message')  # Assuming an element shows the success message
    assert 'Success' in message.text


@then(u'I should see "{name}" in the "Name" field')
def step_impl(context, name):
    name_field = context.browser.find_element(By.ID, 'name')  # Assuming the Name field has an ID
    assert name in name_field.get_attribute('value')


@then(u'I should see "{description}" in the "Description" field')
def step_impl(context, description):
    description_field = context.browser.find_element(By.ID, 'description')  # Assuming the Description field has an ID
    assert description in description_field.get_attribute('value')


@then(u'I should see "{available}" in the "Available" dropdown')
def step_impl(context, available):
    available_dropdown = context.browser.find_element(By.ID, 'available')  # Assuming the Available dropdown has an ID
    assert available in available_dropdown.text


@then(u'I should see "{category}" in the "Category" dropdown')
def step_impl(context, category):
    category_dropdown = context.browser.find_element(By.ID, 'category')  # Assuming the Category dropdown has an ID
    assert category in category_dropdown.text


@then(u'I should see "{price}" in the "Price" field')
def step_impl(context, price):
    price_field = context.browser.find_element(By.ID, 'price')  # Assuming the Price field has an ID
    assert price in price_field.get_attribute('value')
