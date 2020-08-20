import requests
import hashlib
import sys

def request_api_data(query_data):
	url='https://api.pwnedpasswords.com/range/'+query_data
	res=requests.get(url)
	if res.status_code != 200:
		raise RuntimeError(f'error fetching:{res.status_code} error getting api ')
	return res
def count_leaks(hashes,tail):
 	hashes=(line.split(':') for line in hashes.text.splitlines())
 	for h,count in hashes:
 		if h==tail:
 			return count
 	return 0

def pwned_password(password):
	res=hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
	first5,tail=res[:5],res[5:]
	res=request_api_data(first5)
	return count_leaks(res,tail)
	


 

def main(args):
	for password in args:
		res=pwned_password(password)
		if res:
			print(f'your {password} count was {res} times')
		else:
			print('not found')
	return 'done'


if __name__=='__main__':
	sys.exit(main(sys.argv[1:]))