var updateBtns = document.getElementsByClassName('update-cart')

// eventlisteners are just a way for us to deal with
// whenever an user interacts with a button


for(var i = 0; i < updateBtns.length; i++){

// waits when the click func is activated
    updateBtns[i].addEventListener('click', function(){
        var productId = this.dataset.product
        var action = this.dataset.action
        console.log("Product id is ",productId)
        console.log("action is", action)

        console.log("user is ",user)

        if (user == 'AnonymousUser'){
            console.log("Not logged In")
        }
        else
        {
            updateUserOrder(productId, action)
        }



    })

}



function updateUserOrder(productId, action){

}
