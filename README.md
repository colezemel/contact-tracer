Authorization:

1. Get authorization code from authorization page. This is a one-time, manual step. Paste the code below
   in a browser, hit enter then grab the "code" part from the resulting url. Pay attention to scope, different scopes required for different api routes (eg.: scope=read_all for Export Route GPX route)

http://www.strava.com/oauth/authorize?client_id=[YOUR_CLIENT_ID]&response_type=code&redirect_uri=http://localhost/exchange_token&approval_prompt=force&scope=read_all

2. Exchange authorization code for access token & refresh token by making the following POST request with cURL or Postman (client id and secret can be found at https://www.strava.com/settings/api)

https://www.strava.com/oauth/token?client_id=[YOUR_CLIENT_ID]&client_secret=[YOUR_CLIENT_SECRET]&code=[AUTHORIZATION_CODE_FROM_STEP_1]&grant_type=authorization_code

3. Copy your access token and refresh token from the response from Step 2. Need access token for requests, need refresh token to get a new access token when it expires.

---

---

---

---

---

---

---

My Info:

client_id: 47577
client_secret: 0c923040d7b751bb7b67b1089b992a4092adbe2d
authorization_code: 757c84a521b3ae514f13de8de92d398736db2b16

access_token: 1b9c24e9d284d69a88dc3914a5a1fd2032684033
refresh_token: 2d39cf815c2f0d8ac7698eefde29b85f2d015a16
# contact-tracer
