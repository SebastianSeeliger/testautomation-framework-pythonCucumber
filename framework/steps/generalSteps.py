from behave import when


@when('I enter "{value}" in "{item}"')
def step_impl(context, value, item):
    search_box = context.driver.find_element_by_name(item)
    search_box.send_keys(value)

@when('I click "{item}"')
def step_impl(context, item):
    search_button = context.driver.find_element_by_name(item)
    search_button.click()