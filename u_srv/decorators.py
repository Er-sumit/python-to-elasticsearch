import functools

user = {"username": "sumit", "access_level": "guest"}
def make_secure(func):
  #functools.wraps - allows to retain called function properties such as name or documentation, while its secured with @make_secure
  @functools.wraps(func)
  def secure_function(*args, **kwargs):
    if user["access_level"] == "admin":
      return func(*args, **kwargs)
    else:
      return f"No admin permission for {user['username']}"
    
  return secure_function



@make_secure
def get_password(panel):
  if panel == "admin":
    return "1234"
  elif panel == "billing":
    return "ssp"
  
print(get_password("admin"))
