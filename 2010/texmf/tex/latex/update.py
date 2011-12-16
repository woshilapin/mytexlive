import os
import os.path
import subprocess
import re

def file_time(filename):
	try:
		modified_time = os.path.getmtime(filename)
	except OSError:
		modified_time = 0
	return modified_time

path = os.getcwd()
for rep_name in os.listdir(path):
	os.chdir(path)
	if os.path.isdir(rep_name):
		os.chdir(rep_name)
		ins_filename = rep_name + ".ins"
		dtx_filename = rep_name + ".dtx"
		if os.access(ins_filename, os.F_OK):
			ins_file = open(ins_filename, mode='r')
			for line in ins_file:
				print(line)
				if '\\file{' in line:
					out_filename = re.sub(r'^.*\\file{([a-z.]*)}.*', r'\1', line).strip(' \t\n\r')
					if not ( os.access(out_filename, os.F_OK) and file_time(out_filename) >= file_time(ins_filename) and file_time(out_filename) >= file_time(dtx_filename) ):
						subprocess.check_call(["latex", ins_filename])
		pdf_filename = dtx_filename[:-3] + "pdf"
		if os.access(dtx_filename, os.F_OK):
			if not ( os.access(pdf_filename, os.F_OK) and file_time(pdf_filename) >= file_time(dtx_filename) ):
				idx_filename = dtx_filename[:-3] + "idx"
				ind_filename = dtx_filename[:-3] + "ind"
				glo_filename = dtx_filename[:-3] + "glo"
				gls_filename = dtx_filename[:-3] + "gls"
				dvi_filename = dtx_filename[:-3] + "dvi"
				ps_filename = dtx_filename[:-3] + "ps"
				subprocess.check_call(["latex", dtx_filename])
				subprocess.check_call(["makeindex", "-s", "gind.ist", "-o", ind_filename, idx_filename])
				subprocess.check_call(["makeindex", "-s", "gglo.ist", "-o", gls_filename, glo_filename])
				subprocess.check_call(["latex", dtx_filename])
				subprocess.check_call(["makeindex", "-s", "gind.ist", "-o", ind_filename, idx_filename])
				subprocess.check_call(["makeindex", "-s", "gglo.ist", "-o", gls_filename, glo_filename])
				subprocess.check_call(["latex", dtx_filename])
				subprocess.check_call(["latex", dtx_filename])
				subprocess.check_call(["dvips", dvi_filename])
				subprocess.check_call(["ps2pdf", ps_filename])
