
//window.article_id = {{article.id}}

$(document).ready(function(){
$("#upvote").click(function(){
    $.post("/articles/"+window.article_id+"/upvote",
    {},
    function(response){
        $("#vote_count").text(response.votes);
        $("#upvote").style({color:'blue'});
    });

});
$("#upvote").click(function(){
    console.log(5 + 6);
    });
//$("#down").click(function(){
//    var down = $.post("/downvote", {changeBy: 1},
//    function(dataBack){
//        $("#downvote").text(dataBack);
//    });
//
//  });
});