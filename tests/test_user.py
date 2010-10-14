from test_basics import setUp, app

def test_visit_login():
    r = app.get('/mod/login')
    assert "<form name=\"login\"" in r


def test_login():
    r = app.get('/mod/login')
    r.form['username'] = 'admin'
    r.form['password'] = 'adminadmin1'
    r = r.form.submit()
    assert "You are now logged in" in r
