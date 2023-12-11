prompt_template = """


Question: {question}\
The response must ONLY contain the code snippet and NOTHING else.
The response must be one single line which contains only the query and must not be assigned to a variable. 

Make sure you follow the instructions/thought process below. 
Return a pandas DF query based on the question and CSV file schema below. 

Instructions: 
Make sure that the pandas query always accounts for positions which are very similar to the one asked in the question.

Example 1: 
Question: Product Managers
df[df['Position'].str.contains('Product Manager', case=False, na=False)]

Example 2: 
Question: People who work at Google
df[df['Company'].str.contains('Google', case=False, na=False)]

CSV file schema: 
You have access to a LinkedIn connections CSV file which has the first name, last name, URL, Company, Position, and Connected On columns. 

"""