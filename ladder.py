def ladder(steps):

	a = 1

	b = 2

	if steps==1:

		return 1

	else if steps==2:

		return 2

	else:

		for i in range(steps-2):

			c = a+b;

			a = b

			b = c

		return c
