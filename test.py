
def strip_response(response):
    prefix = "Answer: "
    if response.startswith('Answer: '):
        return response[len(prefix):]
    else:
        return response

print(strip_response("Answer: df[df['First Name'].str.contains('Vasu', case=False, na=False) & df['Last Name'].str.contains('Katoch', case=False, na=False)]"))