def log_api_call(func):
    def wrapper(*args,**kwargs):
        print(f"Calling function -{func.__name__}")
        print(f"Arguments={args},Keyword Arguments {kwargs}")
        result=func(*args,**kwargs)
        print(f"Returned: {result}")
        return result

    return wrapper


@log_api_call
def fetch_user(user_id):
    return {"user_id": user_id, "name": "Alice"}


fetch_user(101)


# What Happens Internally:
# Python sees @log_api_call and does this:

# python
# fetch_user = log_api_call(fetch_user)
# So now fetch_user is actually pointing to wrapper.

# When you call fetch_user(101), it runs wrapper(101):

# Logs the function name and arguments

# Calls the original fetch_user(101)

# Logs the result

# Returns the result



