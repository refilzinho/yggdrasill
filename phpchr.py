import cmd

#payload useful to htb lovetok web challenge
class Gen(cmd.Cmd):
	prompt = "query > "
	def default(self, line):
		phpchr(line)


def phpchr(plain):
	payload = ''
	for c in plain:
		payload += "chr({}).".format(ord(c))

	print(payload[:-1])


Gen().cmdloop()
