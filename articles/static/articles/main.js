$(document).ready(function(){
//  home_page article_list
    $.ajax(
        {
            type: "GET",
            url: "/article_list",
            success: function(response){
                var i;
                var article_list = $("#site_article_list");
                var monthNames = [
                        "Jan", "Feb", "Mar",
                        "Apr", "May", "Jun", "Jul",
                        "Aug", "Sep", "Oct",
                        "Nov", "Dec"
                        ];
                var newHours = 0
                var ampm = ""
                for (i = 0; i < response.length; i++) {
                    var user = response[i].created_by.user.username;
                    var d = response[i].created_at;
                    var topic = response[i].topic.topic_name;
                    var year = d.substr(0,4);
                    var month = d.substr(5,2);
                    var date = d.substr(8,2);
                    var hours = d.substr(11,2);
                    var minutes = d.substr(14,2);
                    if (hours<13) {
                        newHours = hours;
                        ampm = " a.m.";
                        } else if (hours === 0) {
                        newHours = 12;
                        ampm = " a.m.";
                        } else {
                        newHours = hours-12;
                        ampm = " p.m.";}
                    var newMonth = monthNames[month-1]
                    var datestring = newMonth+". "+date+", "+year+", "+newHours + ":" + minutes+ampm
                    var output = "<div class=\"container article_lists\"><div class=\"row\"><div class=\"col-md-5\"><a><h2>"
                    +response[i].article_name+
                    "</h2></a></div><div class=\"col-md-2 text-truncate\"><h6>Topic: <a>"
                    +topic+
                    "</a></h6></div><div class=\"col-md-2\"><h6>Created by: <a>"
                    +user+
                    "</a></h6></div><div class=\"col-md-3\"><h6>Created at: "
                    +datestring+
                    "</a></h6></div></div></div>";

                    $('#site_article_list').append(output);
                    }
            },
            dataType: 'json',
            contentType: "application/json; charset=utf-8",
         }
         );
//  article_details comment list
    $.ajax(
        {
            type: "GET",
            url: "/articles/"+window.article_id+"/comment",
            success: function(response){
                var i;
                var comment_list = $("#comment_list");
                var monthNames = [
                        "Jan", "Feb", "Mar",
                        "Apr", "May", "Jun", "Jul",
                        "Aug", "Sep", "Oct",
                        "Nov", "Dec"
                        ];
                var newHours = 0
                var ampm = ""
                for (i = 0; i < response.length; i++) {
                    var user = response[i].commenter.user.username;
                    var d = response[i].time;
                    var year = d.substr(0,4);
                    var month = d.substr(5,2);
                    var date = d.substr(8,2);
                    var hours = d.substr(11,2);
                    var minutes = d.substr(14,2);
                    if (hours<13) {
                        newHours = hours;
                        ampm = " a.m.";
                        } else if (hours === 0) {
                        newHours = 12;
                        ampm = " a.m.";
                        } else {
                        newHours = hours-12;
                        ampm = " p.m.";}
                    var newMonth = monthNames[month-1]
                    var datestring = newMonth+". "+date+", "+year+", "+
                    newHours + ":" + minutes+ampm
                    var output = $("<div class=\"article_details\"><h5>"+response[i].comment_body+"</h5>"+"<h6>Created by: "
                    +user+"</h6><h6>Posted at: "+datestring+"</h6></div>");
                    $('#comment_list').append(output);
                    }
            },
            dataType: 'json',
            contentType: "application/json; charset=utf-8",
         }
         );
//    upvote
    $("#upvote").click(function(){
        $.post("/articles/"+window.article_id+"/upvote",
            {},
            function(response){
                $(".vote_count").text("Votes: " + response.vote_count);
                $("#i-arrow-top").css('color','green');
                $("#i-arrow-bottom").css('color','red');
             });
        });
//    downvote
    $("#downvote").click(function(){
        $.post("/articles/"+window.article_id+"/downvote",
            {},
            function(response){
                $(".vote_count").text("Votes: " + response.vote_count);
                $("#i-arrow-top").css('color','red');
                $("#i-arrow-bottom").css('color','green');
            });
        });
//    update comment list
    $("#comment").click(function(){
        $.ajax(
            {
                type: "POST",
                url: "/articles/"+window.article_id+"/comment",
                data: JSON.stringify({
                    article: window.article_id,
                    comment_body:$("#id_comment_body").val()
                }),
                success: function(response){
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
                    $('#comment_list').prepend(output);
                    $(".empty_list").remove();
                    $("#id_comment_body").val("");
                },
                dataType: 'json',
                contentType: "application/json; charset=utf-8",
             }
             );
        });

    });
