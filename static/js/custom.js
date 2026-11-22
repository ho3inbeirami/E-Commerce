function sendArticleComment(ArticleId) {

    var comment = $('#commentText').val()
    var parent_id = $('#parent_id').val()

    var context = {
        'comment': comment,
        'article_id': ArticleId,
        'parent_id': parent_id
    }

    $.get('add-article-comment/', context).then(
        res => {
            console.log(res)

            document.getElementById('response_area').scrollIntoView({ behavior: 'smooth' })
            $('#commentText').val('')
            $('#parent_id').val('')
            $('#response_area').html(res)
        }
    )
}



function get_patent_id(parent_id) {
    $('#parent_id').val(parent_id)

    document.getElementById('scrollComment').scrollIntoView({ behavior: 'smooth' })

}


function SendDataFilterPrice() {
    var start_price = $("#sl2").val().split(',')[0]
    var end_price = $("#sl2").val().split(',')[1]
    $('#start_price').val(start_price)
    $('#end_price').val(end_price)
    console.log(start_price)
    
}


function FillPage(page){
    $('#').val(page)
}

function replaecImage(imageurl){ 
    $('#mainImage').attr('src', imageurl)
}



function AddToShoppingCart(productId){
    var count = $("#ProductCount").val()
    console.log(count)
    console.log(productId)
    $.get('/add_product_to_order?productId='+productId+'&count='+count).then(
        res => {
            console.log(res)

            Swal.fire({
                title: res.title ,
                text: res.text,
                icon: res.icon,
                showConfirmButton: true
            });
            return res
        }
    )
    
    

}






function removeItem (productId){
    console.log('remove item')
    console.log(productId)
    $.get('/remove_item_from_cart?productId='+productId)

    $.get('/remove_item_from_cart?productId='+productId).then(
        res=>{
            if (res.status=='success') {
                console.log(res.status)
                $("#cartComponent").html(res.data)
            }
        }
    )
}


function changeCountItem(productId, number){
    console.log(number)
    console.log(productId)
    $.get('/change_count_item_from_cart?productId='+productId+'&increase='+number).then(
        res=>{
            if (res.status=='success') {
                console.log(res.status)
                $("#cartComponent").html(res.data)
            }
        }
    )

}
