from test_basics import setUp, app

def test_visit_login():
    r = app.get('/login')
    assert "<form name=\"login\"" in r


def test_login():
    r = app.get('/login')
    r.form.username = 'admin'
    r.form.password = 'adminadmin1'
    r = r.form.submit()
