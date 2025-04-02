import tiktoken

txt = "1 2 3 1998 1975 2000 나는 한국인 입니다. I am a boy."
enc = tiktoken.get_encoding("gpt2")
assert enc.decode(enc.encode("hello world")) == "hello world"

print("token ids=", enc.encode(txt))
for (i, t) in enumerate(enc.encode(txt)):
	print(f"[{i:02d}] => \t[{t}] => \t[{enc.decode([t])}]")

enc = tiktoken.encoding_for_model("gpt-4o")
print("token ids=", enc.encode(txt))

for (i, t) in enumerate(enc.encode(txt)):
	print(f"[{i:02d}] => \t[{t}] => \t[{enc.decode([t])}]")

