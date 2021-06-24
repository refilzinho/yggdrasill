import cmd
import base64

class Gen(cmd.Cmd):
	prompt = "query > "

	def default(self, line):
		base64gen(line)


def base64gen(plain):
	plain_bytes    = plain.encode('ascii')
	base64_bytes   = base64.b64encode(plain_bytes)

	print(str(base64_bytes))


Gen().cmdloop()
