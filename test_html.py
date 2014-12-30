import os, sys


f = open('/www/sites/crazyforus.com/aggregator/templates/aggregator/article-1.html')
html_file = f.read()
html_file = html_file[:6000]
limit = html_file.count("<")
for i in range(1,limit):
		start = html_file.find("<")
		end = html_file.find(">")
		if end > 0:
				end = end+1
				slice_len = (end-start)
				repl_str = html_file[start:end]
				html_file = html_file[:start] + html_file[end:]
				html_file = html_file.replace("\r", "")
				html_file = html_file.replace("\n", "")
		else:
				break
print html_file
