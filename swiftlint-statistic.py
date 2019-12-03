f = open("swiftlint.log")
items = f.readlines()
f.close()

violations = dict()
for item in items:
	parts = item.split(":")
	filename = parts[0]
	row = parts[1]
	col = parts[2]
	violationLevel = parts[3]
	violationType = parts[4].strip()
	violationDesc = parts[5]
	if violationType in violations:
		count = violations.get(violationType)
		violations[violationType] = count + 1
	else:
		violations[violationType] = 1

print(violations)