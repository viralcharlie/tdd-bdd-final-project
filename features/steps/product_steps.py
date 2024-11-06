#from behave import when, then
#from selenium.webdriver.common.by import By
#from selenium.webdriver.support.ui import Select
#import time  # Optional, if waiting for elements to load is necessary

import logging
from behave import when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions

# Assuming `context.browser` is the initialized Selenium WebDriver

# Scenario: The server is running

@when('I visit the "{page_name}"')
def step_impl(context, page_name):
    if page_name == "Home Page":
        context.browser.get(context.base_url)
    #time.sleep(1)  # Wait for the page to load (optional)

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
    #time.sleep(1)  # Wait for any action to complete (optional)

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
    #time.sleep(1)

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

#Scenario Update a product
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


@then(u'I should see "{description}" in the "Description" field')
def step_impl(context, description):
    description_field = context.browser.find_element(By.ID, 'description')  # Assuming the Description field has an ID
    assert description in description_field.get_attribute('value')


@when(u'I change "Name" to "{new_name}"')
def step_impl(context, new_name):
    name_field = context.browser.find_element(By.ID, 'name')  # Assuming the ID for the name field
    name_field.clear()  # Clear the existing name
    name_field.send_keys(new_name)


@when(u'I press the "Update" button')
def step_impl(context):
    update_button = context.browser.find_element(By.XPATH, '//button[contains(text(), "Update")]')
    update_button.click()


@then(u'I should see the message "Success"')
def step_impl(context):
    message = context.browser.find_element(By.ID, 'message')  # Assuming an element that displays the success message
    assert 'Success' in message.text


@when(u'I copy the "Id" field')
def step_impl(context):
    id_field = context.browser.find_element(By.ID, 'id')  # Assuming the ID for the product field
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
    message = context.browser.find_element(By.ID, 'message')  # Assuming an element that displays the success message
    assert 'Success' in message.text


@then(u'I should see "{new_name}" in the "Name" field')
def step_impl(context, new_name):
    name_field = context.browser.find_element(By.ID, 'name')  # Assuming the Name field has an ID
    assert new_name in name_field.get_attribute('value')


@when(u'I press the "Search" button')
def step_impl(context):
    search_button = context.browser.find_element(By.XPATH, '//button[contains(text(), "Search")]')
    search_button.click()


@then(u'I should see "{new_name}" in the results')
def step_impl(context, new_name):
    result = context.browser.find_element(By.XPATH, f'//li[contains(text(), "{new_name}")]')  # Assuming the result appears in a list
    assert new_name in result.text


@then(u'I should not see "{old_name}" in the results')
def step_impl(context, old_name):
    try:
        context.browser.find_element(By.XPATH, f'//li[contains(text(), "{old_name}")]')
        assert False, f'{old_name} should not be in the results'
    except NoSuchElementException:
        pass  # If the old name is not found, the test passes

#Scenario Delete a product
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


@then(u'I should see "{description}" in the "Description" field')
def step_impl(context, description):
    description_field = context.browser.find_element(By.ID, 'description')  # Assuming the Description field has an ID
    assert description in description_field.get_attribute('value')


@when(u'I copy the "Id" field')
def step_impl(context):
    id_field = context.browser.find_element(By.ID, 'id')  # Assuming the ID for the product field
    context.copied_id = id_field.get_attribute('value')


@when(u'I press the "Clear" button')
def step_impl(context):
    clear_button = context.browser.find_element(By.XPATH, '//button[contains(text(), "Clear")]')
    clear_button.click()


@when(u'I paste the "Id" field')
def step_impl(context):
    id_field = context.browser.find_element(By.ID, 'id')  # Assuming an ID field exists to paste the ID
    id_field.send_keys(context.copied_id)


@when(u'I press the "Delete" button')
def step_impl(context):
    delete_button = context.browser.find_element(By.XPATH, '//button[contains(text(), "Delete")]')
    delete_button.click()


@then(u'I should see the message "Product has been Deleted!"')
def step_impl(context):
    message = context.browser.find_element(By.ID, 'message')  # Assuming an element that displays the success message
    assert 'Product has been Deleted!' in message.text


@when(u'I press the "Search" button')
def step_impl(context):
    search_button = context.browser.find_element(By.XPATH, '//button[contains(text(), "Search")]')
    search_button.click()


@then(u'I should see the message "Success"')
def step_impl(context):
    message = context.browser.find_element(By.ID, 'message')  # Assuming there's an ID for the message element
    assert 'Success' in message.text


@then(u'I should not see "{product_name}" in the results')
def step_impl(context, product_name):
    try:
        context.browser.find_element(By.XPATH, f'//li[contains(text(), "{product_name}")]')  # Searching for product name in the results
        assert False, f'{product_name} should not be in the results'
    except NoSuchElementException:
        pass  # If the product name is not found, the test passes

#Scenario List all Products
@when(u'I visit the "Home Page"')
def step_impl(context):
    context.browser.get(f'{context.base_url}/')  # Assuming the home page is the base URL


@when(u'I press the "Clear" button')
def step_impl(context):
    clear_button = context.browser.find_element(By.XPATH, '//button[contains(text(), "Clear")]')
    clear_button.click()


@when(u'I press the "Search" button')
def step_impl(context):
    search_button = context.browser.find_element(By.XPATH, '//button[contains(text(), "Search")]')
    search_button.click()


@then(u'I should see the message "Success"')
def step_impl(context):
    message = context.browser.find_element(By.ID, 'message')  # Assuming there's an ID for the message element
    assert 'Success' in message.text


@then(u'I should see "{product_name}" in the results')
def step_impl(context, product_name):
    try:
        context.browser.find_element(By.XPATH, f'//li[contains(text(), "{product_name}")]')  # Searching for product name in the results
    except NoSuchElementException:
        assert False, f'{product_name} should be in the results'


# To verify multiple products in one go, we can extend the functionality:
@then(u'I should see the following products in the results')
def step_impl(context):
    products = ["Hat", "Shoes", "Big Mac", "Sheets"]
    for product in products:
        try:
            context.browser.find_element(By.XPATH, f'//li[contains(text(), "{product}")]')
        except NoSuchElementException:
            assert False, f'{product} should be in the results'


#Scenario Search by Category
@when(u'I visit the "Home Page"')
def step_impl(context):
    context.browser.get(f'{context.base_url}/')  # Assuming the home page is the base URL


@when(u'I press the "Clear" button')
def step_impl(context):
    clear_button = context.browser.find_element(By.XPATH, '//button[contains(text(), "Clear")]')
    clear_button.click()


@when(u'I select "{category}" in the "Category" dropdown')
def step_impl(context, category):
    category_dropdown = context.browser.find_element(By.NAME, 'category')  # Assuming the dropdown has a name attribute
    category_dropdown.click()  # Click the dropdown to reveal options
    category_option = context.browser.find_element(By.XPATH, f'//option[text()="{category}"]')
    category_option.click()  # Select the desired category


@when(u'I press the "Search" button')
def step_impl(context):
    search_button = context.browser.find_element(By.XPATH, '//button[contains(text(), "Search")]')
    search_button.click()


@then(u'I should see the message "Success"')
def step_impl(context):
    message = context.browser.find_element(By.ID, 'message')  # Assuming there's an ID for the message element
    assert 'Success' in message.text


@then(u'I should see "{product_name}" in the results')
def step_impl(context, product_name):
    try:
        context.browser.find_element(By.XPATH, f'//li[contains(text(), "{product_name}")]')  # Searching for product name in the results
    except NoSuchElementException:
        assert False, f'{product_name} should be in the results'


@then(u'I should not see "{product_name}" in the results')
def step_impl(context, product_name):
    try:
        context.browser.find_element(By.XPATH, f'//li[contains(text(), "{product_name}")]')  # Searching for product name in the results
        assert False, f'{product_name} should NOT be in the results'
    except NoSuchElementException:
        pass  # If the product is not found, it’s correct that it is not in the results

#Scenario Search by Available
@when(u'I visit the "Home Page"')
def step_impl(context):
    context.browser.get(f'{context.base_url}/')  # Assuming the home page is the base URL


@when(u'I press the "Clear" button')
def step_impl(context):
    clear_button = context.browser.find_element(By.XPATH, '//button[contains(text(), "Clear")]')
    clear_button.click()


@when(u'I select "{availability}" in the "Available" dropdown')
def step_impl(context, availability):
    available_dropdown = context.browser.find_element(By.NAME, 'available')  # Assuming the dropdown has a name attribute
    available_dropdown.click()  # Click the dropdown to reveal options
    available_option = context.browser.find_element(By.XPATH, f'//option[text()="{availability}"]')
    available_option.click()  # Select the desired availability option


@when(u'I press the "Search" button')
def step_impl(context):
    search_button = context.browser.find_element(By.XPATH, '//button[contains(text(), "Search")]')
    search_button.click()


@then(u'I should see the message "Success"')
def step_impl(context):
    message = context.browser.find_element(By.ID, 'message')  # Assuming there's an ID for the message element
    assert 'Success' in message.text


@then(u'I should see "{product_name}" in the results')
def step_impl(context, product_name):
    try:
        context.browser.find_element(By.XPATH, f'//li[contains(text(), "{product_name}")]')  # Searching for product name in the results
    except NoSuchElementException:
        assert False, f'{product_name} should be in the results'


@then(u'I should not see "{product_name}" in the results')
def step_impl(context, product_name):
    try:
        context.browser.find_element(By.XPATH, f'//li[contains(text(), "{product_name}")]')  # Searching for product name in the results
        assert False, f'{product_name} should NOT be in the results'
    except NoSuchElementException:
        pass  # If the product is not found, it’s correct that it is not in the results

#Scenario by Name
@when(u'I visit the "Home Page"')
def step_impl(context):
    context.browser.get(f'{context.base_url}/')  # Assuming the home page is the base URL


@when(u'I set the "Name" to "{product_name}"')
def step_impl(context, product_name):
    name_field = context.browser.find_element(By.NAME, 'name')  # Assuming the "Name" field has a name attribute
    name_field.clear()  # Clear any existing input
    name_field.send_keys(product_name)  # Enter the product name to search for


@when(u'I press the "Search" button')
def step_impl(context):
    search_button = context.browser.find_element(By.XPATH, '//button[contains(text(), "Search")]')
    search_button.click()


@then(u'I should see the message "Success"')
def step_impl(context):
    message = context.browser.find_element(By.ID, 'message')  # Assuming there's an ID for the message element
    assert 'Success' in message.text


@then(u'I should see "{product_name}" in the "Name" field')
def step_impl(context, product_name):
    name_field = context.browser.find_element(By.NAME, 'name')  # Assuming the "Name" field has a name attribute
    assert product_name in name_field.get_attribute('value')


@then(u'I should see "{description}" in the "Description" field')
def step_impl(context, description):
    description_field = context.browser.find_element(By.NAME, 'description')  # Assuming the "Description" field has a name attribute
    assert description in description_field.get_attribute('value')
