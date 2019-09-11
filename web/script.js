// Create a request variable and assign a new XMLHttpRequest object to it.
var request = new XMLHttpRequest()

// Open a new connection, using the GET request on the URL endpoint
request.open('GET', 'http://localhost:8080/content', true)

request.onload = function () {
  // Begin accessing JSON data here
  var data = JSON.parse(this.response)
  console.log(data)

  if (request.status >= 200 && request.status < 400) {
    for (var k in data) {
      console.log("Key:" + k);
      console.log("Value:" + data[k]);
    }
  } else {
    console.log('error')
  }
}

// Send request
request.send()
