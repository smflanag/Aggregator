

$(document).ready(function(){
    $("#upvote").click(function(){
        $.post("/articles/"+window.article_id+"/upvote",
            {},
            function(response){
                $(".vote_count").text("Votes: " + response.vote_count);
                $("#i-arrow-top").css('color','green');
                $("#i-arrow-bottom").css('color','red');
             });
        });
    $("#downvote").click(function(){
        $.post("/articles/"+window.article_id+"/downvote",
            {},
            function(response){
                $(".vote_count").text("Votes: " + response.vote_count);
                $("#i-arrow-top").css('color','red');
                $("#i-arrow-bottom").css('color','green');
            }
        );
    });
    });
