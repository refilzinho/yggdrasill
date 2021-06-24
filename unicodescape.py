import cmd


class Gen(cmd.Cmd):
	prompt = "query > "

	def default(self, line):
		unicodescape(line)

def unicodescape(query):
	payload = ''

	for c in query:
		payload += r"\u{:04x}".format(ord(c))
	
	print(payload)

Gen().cmdloop()