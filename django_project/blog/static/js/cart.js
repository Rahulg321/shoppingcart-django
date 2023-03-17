var updateBtns = document.getElementsByClassName('update-cart')

// eventlisteners are just a way for us to deal with
// whenever an user interacts with a button


for (var i = 0; i < updateBtns.length; i++) {

    // waits when the click func is activated
    updateBtns[i].addEventListener('click', function () {
        // whenever a user clicks fetch the product id and action associated with that particular button
        var productId = this.dataset.product
        var action = this.dataset.action
        console.log("Product id is ", productId)
        console.log("action is", action)

        console.log("user is ", user)

        if (user == 'AnonymousUser') {
            console.log("Not logged In")
        }
        else {
            // if a user is indeed logged in, perform the updateitem function
            updateUserOrder(productId, action)
        }

    })

}



// way to send Json data between different views and templates

function updateUserOrder(productId, action) {
    console.log("Sending data user is logged in")
    //basically we are sending our product id and the action associated with it to our view 
    // sending it in json format as a POST request
    var url = '/update-item/'

    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFTOKEN': csrftoken,
        },
        body: JSON.stringify({ 'productId': productId, 'action': action })
    })

        .then((response) => {
            return response.json()
        })

        .then((data) => {
            console.log('data: ', data)
            location.reload()
        })
}
