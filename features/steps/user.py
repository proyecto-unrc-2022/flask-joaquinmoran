import json
from behave import *
from application import USERS


@given('some users are in the system')
def step_impl(context):
    USERS.update({'jasonb': {'name': 'Jason Bourne'}})

@when(u'I retrieve the customer \'jasonb\'')
def step_impl(context):
    context.page = context.client.get('/users/{}'.format('jasonb'))
    assert context.page

@then('I should get a \'200\' response')
def step_impl(context):
    assert context.page.status_code is 200

@then(u'the following user details are returned')
def step_impl(context):
    # assert context.table[0].cells[0] in context.page.text
    assert "Jason Bourne" in context.page.text

#Start of the second scenario-----------------------------------------------------------------------

@given('a user that is not in the system')
def step_impl(context):
    user_in = USERS.get('johnl', 'Not in')
    assert user_in is 'Not in'

@when(u'add the new user \'John Lennon\'')
def step_impl(context):
    body = {'johnl':{'name': 'John Lennon'}}
    headers = {'Content-Type': 'application/json'}
    context.res = context.client.post('/users/logguser', data=json.dumps(body), headers=headers)
    print(context.res.text)
    assert context.res

@then(u'get a \'200\' response')
def step_impl(context):
    assert context.res.status_code is 200

@then(u'the following user are returned')
def step_impp(context):
    assert "John Lennon" in context.res.text

#Start of the third scenario------------------------------------------------------------------------

@given('users stored in the system')
def step_impl(context):
    USERS.update({'paulm':{'name': 'Paul McCartney'}})

@when(u'retrieve the customer \'Paul McCartney\'')
def step_impl(context):
    body = {'paulm':{'name':'James Paul McCartney'}}
    headers = {'Content-Type': 'application/json'}
    context.up = context.client.put('/users/updateuser', data=json.dumps(body), headers=headers)
    print(USERS)
    assert context.up

@then(u'get \'200\' as response')
def step_impl(context):
    assert context.up.status_code is 200

@then(u'the following info. should be returned')
def step_impl(context):
    assert 'James Paul McCartney' in context.up.text

#Start of the fourth scenario-----------------------------------------------------------------------

@given('users in the system')
def step_impl(context):
    USERS.update({'peterb' :{'name': 'Peter Best'}})

@when(u'retrieve the customer \'Peter Best\'')
def step_impl(context):
    headers = {'Content-Type': 'application/json'}
    context.dele = context.client.delete('/users/delete/{}'.format('peterb'), headers = headers)
    assert context.dele

@then(u'obtain a \'200\' response')
def step_impl(context):
    assert context.dele.status_code is 200

@then(u'the following information')
def step_impl(context):
    assert 'Peter Best' not in USERS

#Start of the fifth scenario------------------------------------------------------------------------

@given('a list of customers stored in the system')
def step_impl(context):
    assert USERS

@when(u'i want to show them')
def step_impl(context):
    context.list = context.client.get('/users/all/{}'.format(USERS))
    assert context.list

@then(u'i want a \'200\' response')
def step_impl(context):
    assert context.list.status_code is 200

@then(u'the following list')
def step_impl(context):
    assert USERS






   

