import tiktoken

enc = tiktoken.encoding_for_model("gpt-4o")

user_input = input("Enter some text ")
#Eg - Hi I am Kong.
print(f" user_input {user_input}")

tokens = enc.encode(user_input)
#Eg - [12194, 357, 939, 23911, 13]

print(f" Tokens {tokens}")

dec = enc.decode(tokens)

print(f" String {dec}")
#Eg - Hi I am Kong.
