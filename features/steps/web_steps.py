from behave import when, then
from flask import Flask

@when('I click on the "{button}" button')
def step_impl(context, button):
    # Simulating button click action
    pass

@then('I should see "{text}" on the page')
def step_impl(context, text):
    assert text in context.browser.page_source

@then('I should not see "{text}" on the page')
def step_impl(context, text):
    assert text not in context.browser.page_source

@then('I should see a message "{message}"')
def step_impl(context, message):
    assert message in context.browser.page_source
 
