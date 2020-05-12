Authorization:

1. Get authorization code from authorization page. This is a one-time, manual step. Paste the code below in a browser, hit enter then grab the "code" part from the resulting url. Pay attention to scope, different scopes required for different api routes (eg.: scope=read_all for Export Route GPX route)<br />http://www.strava.com/oauth/authorize?client_id=[YOUR_CLIENT_ID]&response_type=code&redirect_uri=http://localhost/exchange_token&approval_prompt=force&scope=read_all

2. Exchange authorization code for access token & refresh token by making the following POST request with cURL or Postman (client id and secret can be found at https://www.strava.com/settings/api)<br />https://www.strava.com/oauth/token?client_id=[YOUR_CLIENT_ID]&client_secret=[YOUR_CLIENT_SECRET]&code=[AUTHORIZATION_CODE_FROM_STEP_1]&grant_type=authorization_code

3. Copy your access token and refresh token from the response from Step 2. Need access token for requests, need refresh token to get a new access token when it expires. Make following POST request to use refresh token from Step 2 to get a new access token:<br />https://www.strava.com/oauth/token?client_id=your_client_id&client_secret=your_client_secret&refresh_token=your_refresh_token_from_previous_step&grant_type=refresh_token
