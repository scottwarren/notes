

1. Take gif URL as a query parameter
2. Make request to get token for auth 
3. Fetch token from request
4. Get JSON details of the video
5. Send a redirect 302 to the media files (SD or HD idk)
6. Create shortcut to call this service with the redgifs url from the share menu)

  

Add a query that tests each stage and alerts if any of the query formats are in an unexpected format


1. Get GIFs URL to use as an example
	1. Using URL, determine how to get the JSON back
	2. Understand authentication
	3. Proxy?
2. Understand how iPhone works when presented with media (I want it to save to photos, not downloads)
	1. Shortcuts?
3. Alerting
	1. if redirect is failing
	2. if auth is failing
	3. if shape of data changes
4. Tests
	1. For expected shape
	2. Authentication
	3. 