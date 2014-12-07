# plus.py (by Wesley Chun under CC-SA3.0 license)
from apiclient import discovery
import sys

if len(sys.argv) < 2:
    sys.exit('Usage: %s search-string' % sys.argv[0])


API_KEY = 'AIzaSyCjYxlLHP5S72bejaM2B_Y3on7obDUPhLo'
service = discovery.build("plus", "v1", developerKey=API_KEY)
feed = service.activities().search(query=sys.argv[1]).execute()
for record in feed['items']:
    post = ' '.join(record['title'].strip().split())
    if post:
        print '\nFrom:', record['actor']['displayName']
        print 'Post:', post
        print 'URL:',record['object']['url']
        print 'Date:', record['published']
