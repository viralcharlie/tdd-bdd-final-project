from behave import when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time  # Optional, if waiting for elements to load is necessary

# Assuming `context.browser` is the initialized Selenium WebDriver

# Scenario: The server is running

@when('I visit the "{page_name}"')
def step_impl(context, page_name):
    if page_name == "Home Page":
        context.browser.get(context.base_url)
    time.sleep(1)  # Wait for the page to load (optional)

@then('I should see "{text}" in the title')
def step_impl(context, text):
    assert text in context.browser.title, f'Expected "{text}" in the title, but got "{context.browser.title}"'

@then('I should not see "404 Not Found"')
def step_impl(context):
    assert "404 Not Found" not in context.browser.page_source, 'Unexpected "404 Not Found" on the page'


# Scenario: Create a Product

@when('I set the "{field_name}" to "{value}"')
def step_impl(context, field_name, value):
    field = context.browser.find_element(By.ID, field_name.lower())  # Adjust selector as needed
    field.clear()
    field.send_keys(value)

@when('I select "{value}" in the "{dropdown_name}" dropdown')
def step_impl(context, value, dropdown_name):
    dropdown = Select(context.browser.find_element(By.ID, dropdown_name.lower()))  # Adjust selector as needed
    dropdown.select_by_visible_text(value)

@when('I press the "{button_text}" button')
def step_impl(context, button_text):
    button = context.browser.find_element(By.XPATH, f"//button[contains(text(), '{button_text}')]")  # Adjust selector as needed
    button.click()
    time.sleep(1)  # Wait for any action to complete (optional)

@then('I should see the message "{message}"')
def step_impl(context, message):
    assert message in context.browser.page_source, f'Expected message "{message}" not found in page source'

@when('I copy the "{field_name}" field')
def step_impl(context, field_name):
    field = context.browser.find_element(By.ID, field_name.lower())
    context.copied_value = field.get_attribute("value")

@when('I press the "Clear" button')
def step_impl(context):
    clear_button = context.browser.find_element(By.XPATH, "//button[contains(text(), 'Clear')]")  # Adjust selector as needed
    clear_button.click()
    time.sleep(1)

@then('the "{field_name}" field should be empty')
def step_impl(context, field_name):
    field = context.browser.find_element(By.ID, field_name.lower())
    assert field.get_attribute("value") == "", f'Expected {field_name} field to be empty'

@when('I paste the "{field_name}" field')
def step_impl(context, field_name):
    field = context.browser.find_element(By.ID, field_name.lower())
    field.clear()
    field.send_keys(context.copied_value)

@then('I should see "{value}" in the "{field_name}" field')
def step_impl(context, value, field_name):
    field = context.browser.find_element(By.ID, field_name.lower())
    assert field.get_attribute("value") == value, f'Expected {field_name} to be "{value}", but got "{field.get_attribute("value")}"'

@then('I should see "{value}" in the "{dropdown_name}" dropdown')
def step_impl(context, value, dropdown_name):
    dropdown = Select(context.browser.find_element(By.ID, dropdown_name.lower()))
    selected_option = dropdown.first_selected_option
    assert selected_option.text == value, f'Expected {dropdown_name} to be "{value}", but got "{selected_option.text}"'
