from datetime import datetime

time = datetime.now()

# Note - f"": f-string (formatted string literal)
# allows you to embed expressions inside string literals. (flags in printf)

formatted_output = f"Seconds since January 1, 1970: {time.timestamp():,.4f} or {time.timestamp():.2e} in scientific notation"

print(formatted_output)
print(time.strftime("%b %d %Y"))
