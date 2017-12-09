def shorten(s, subs):
	while subs in s:
		i = s.index(subs)
		s = s[:i] + s[i+2:]
	return s

def clean(s):
	garbage_total = 0
	while '<' in s and '>' in s:
		i = s.index('<')
		j = s.index('>')
		garbage_total += j - i - 1
		s = s[:i] + s[j+1:]

	print('total garbage : ', garbage_total)
	return s.replace(',', '')

def total_score(s):
	pts = 0
	while '{}' in s:
		i = s.index('{}')
		pts += s[:i+1].count('{')
		s = s.replace('{}', '', 1)
	return pts

with open('data/AoC_9.txt', newline='') as f:
	line = next(f)
	short = shorten(line, '!')
	clean = clean(short)
	print(total_score(clean))
