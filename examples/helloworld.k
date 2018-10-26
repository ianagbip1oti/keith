
# method definition
def print(str):
  # extern block allows us to embed code from other languages
  # :python is a symbol (ruby syntax) indicating the language
  extern :python:
  
    # This print is python's print, not the print method we've defined
    print(str)
 
print("Hello World")
