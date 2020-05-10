// function getRoute(res) {
//   const routeLink =
//     "https://www.strava.com/api/v3/routes/1/export_gpx?access_token=3d0c2ddfda5c98351f13d0e12ec26bc3b716a915";
//   fetch(routeLink).then(res => console.log(res.json));
// }

// getRoute();

const auth_link = "https://www.strava.com/oauth/token";

function getRoute(res) {
  const route_link =
    "https://www.strava.com/api/v3/athlete/activities?access_token=${res.access_token}";
  fetch(route_link).then(res => console.log(res.json()));
}

function reAuthorize() {
  fetch(auth_link, {
    method: "post",
    headers: {
      Accept: "application/json, text/plain, */*",
      "Content-Type": "application/json"
    },

    body: JSON.stringify({
      client_id: "47577",
      client_secret: "0c923040d7b751bb7b67b1089b992a4092adbe2d",
      refresh_token: "390eea5471370e9d896fe5b2ed15e75bcf8a8a27",
      grant_type: "refresh_token"
    })
  }).then(res => getRoute(res));
}

reAuthorize();
