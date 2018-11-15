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
            });
        });
    $("#comment").click(function(){
        $.ajax(
            {
                type: "POST",
                url: "/articles/"+window.article_id+"/comment",
                data: JSON.stringify({
                    commenter:window.user_id,
                    article: window.article_id,
                    comment_body:$("#id_comment_body").val()

                }),
                success: function(response){
                    console.log(5);
                    var comment_body = $("#id_comment_body").val();
                    var d = new Date();
                    var hours = d.getHours()
                    var newHours = 0
                    var ampm = ""
                    if (hours<13) {
                        newHours = hours;
                        ampm = " a.m.";
                        } else if (hours === 0) {
                        newHours = 12;
                        ampm = " a.m.";
                        } else {
                        newHours = hours-12;
                        ampm = " p.m.";}
                    var month = d.getMonth()
                    var monthNames = [
                        "Jan", "Feb", "Mar",
                        "Apr", "May", "Jun", "Jul",
                        "Aug", "Sep", "Oct",
                        "Nov", "Dec"
                        ];
                    var newMonth = monthNames[month]
                    var datestring = newMonth+". "+d.getDate()+", "+d.getFullYear()+", "+
                    newHours + ":" + d.getMinutes()+ampm
                    var output = $("<div class=\"article_details\"><h5>"+comment_body+"</h5>"+"<h6>Created by: "
                    +window.user+"</h6><h6>Posted at: "+datestring+"</h6></div>");
                    $('.comment_list').prepend(output);
                },
                dataType: 'json',
                contentType: "application/json; charset=utf-8",
             }
             );
        });
    });
