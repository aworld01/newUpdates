def basic_tokenize(text):
    text = text.lower().strip()
    tokens = text.split()          # split on whitespace
    return tokens
    
    
data = "I like ball because I like cricket"

print(basic_tokenize(data))