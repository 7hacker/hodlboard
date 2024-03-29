function get_content() {
  // Create a request variable and assign a new XMLHttpRequest object to it.
  var request = new XMLHttpRequest()

  // Open a new connection, using the GET request on the URL endpoint
  request.open('GET', 'http://0.0.0.0:8080/message', true)

  request.onload = function () {
    // Begin accessing JSON data here
    var data = JSON.parse(this.response)
    for (var k in data) {
         console.log("Key:" + k);
         console.log("Value:" + data[k]);
    }
    if (request.status >= 200 && request.status < 400) {
      for (var k in data) {
        card = data[k]
        const app = document.getElementById('content')
        const container = document.createElement('div')
        container.setAttribute('class', 'card-container')
        //Card header
        const card_header = document.createElement('div')
        card_header.setAttribute('class', 'card-header')


        //card content
        const card_content = document.createElement('div')
        card_content.setAttribute('class', 'card-content')
        const p = document.createElement('p')
        p.textContent = `${card.message}...`
        card_content.appendChild(p)

        //card_header and card_content is a child to card-container
        container.appendChild(card_header)
        container.appendChild(card_content)
        app.appendChild(container)
      }
      for (var i = 0; i < 10; i++) {
        const app = document.getElementById('content')
        const container = document.createElement('div')
        container.setAttribute('class', 'filling-empty-space-childs')
        app.appendChild(container)
      }
      // for (var k in data) {
      //   console.log("Key:" + k);
      //   console.log("Value:" + data[k]);
      // }

    } else {
      console.log('error')
    }
  }
  // Send request
  request.send()
}
