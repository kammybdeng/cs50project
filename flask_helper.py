from functools import wraps
from flask import redirect, session, flash

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            flash('Please Login First', 'danger')
            return redirect('login')
        return f(*args, **kwargs)
    return decorated_function
