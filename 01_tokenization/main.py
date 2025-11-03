import tiktoken

enc = tiktoken.encoding_for_model("gpt-4o")

text = "Hey there! I am Goku"
tokens = enc.encode(text)

#Tokens [25216, 1354, 0, 357, 939, 499, 13454]
print(f"Tokens {tokens}")
