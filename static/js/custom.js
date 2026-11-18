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