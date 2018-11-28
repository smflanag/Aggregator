$(document).ready(function(){
//modal contact form
    var modal_init = function() {

    var modalWrapper = document.getElementById("modal_wrapper");
    var modalWindow  = document.getElementById("modal_window");

    var openModal = function(e)
    {
      modalWrapper.className = "overlay";
      var overflow = modalWindow.offsetHeight - document.documentElement.clientHeight;
      if(overflow > 0) {
        modalWindow.style.maxHeight = (parseInt(window.getComputedStyle(modalWindow).height) - overflow) + "px";
      }
      modalWindow.style.marginTop = (-modalWindow.offsetHeight)/2 + "px";
      modalWindow.style.marginLeft = (-modalWindow.offsetWidth)/2 + "px";
      e.preventDefault ? e.preventDefault() : e.returnValue = false;
    };

    var closeModal = function(e)
    {
      modalWrapper.className = "";
      e.preventDefault ? e.preventDefault() : e.returnValue = false;
    };

    var clickHandler = function(e) {
      if(!e.target) e.target = e.srcElement;
      if(e.target.tagName == "DIV") {
        if(e.target.id != "modal_window") closeModal(e);
      }
    };

    var keyHandler = function(e) {
      if(e.keyCode == 27) closeModal(e);
    };

    if(document.addEventListener) {
      document.getElementById("modal_open").addEventListener("click", openModal, false);
      document.getElementById("modal_close").addEventListener("click", closeModal, false);
      document.addEventListener("click", clickHandler, false);
      document.addEventListener("keydown", keyHandler, false);
    } else {
      document.getElementById("modal_open").attachEvent("onclick", openModal);
      document.getElementById("modal_close").attachEvent("onclick", closeModal);
      document.attachEvent("onclick", clickHandler);
      document.attachEvent("onkeydown", keyHandler);
    }

  };
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
                var newHours = 0;
                var ampm = "";
                var template = $('#article_template').html();
                for (i = 0; i < response.length; i++) {

                    var d = response[i].created_at;
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
                    var datestring = newMonth+". "+date+", "+year+", "+newHours + ":" + minutes+ampm;
                    var view = {
                          user: response[i].created_by.user.username,
                          topic: response[i].topic.topic_name,
                          topic_slug: response[i].topic.topic_name.replace(/ /g,"-").toLowerCase(),
                          time: datestring,
                          article: response[i].article_name,
                          article_slug: response[i].article_name.replace(/ /g,"-").toLowerCase()
                        };

                    Mustache.parse(template);
                    var output = Mustache.render(template, view);
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
                var template = $('#comment_template').html();
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
                    var datestring = newMonth+". "+date+", "+year+", "+newHours + ":" + minutes+ampm
                    var view = {
                          comment_body: response[i].comment_body,
                          user: user,
                          datestring: datestring
                        };
                    Mustache.parse(template);
                    var output = Mustache.render(template, view);
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
                    var newHours = 0;
                    var ampm = "";
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
                    var newMonth = monthNames[month];
                    var datestring = newMonth+". "+d.getDate()+", "+d.getFullYear()+", "+
                    newHours + ":" + d.getMinutes()+ampm;
                    var output = "<div class=\"article_details\"><h5>"+comment_body+"</h5>"+"<h6>Created by: "+window.user+"</h6><h6>Posted at: "+datestring+"</h6></div>";
                    $('#comment_list').prepend(output);
                    $(".empty_list").remove();
                    $("#id_comment_body").val("");
                },
                dataType: 'json',
                contentType: "application/json; charset=utf-8",
             }
             );
        });
// contact form
    $("#feedbackForm").click(function(){
        $.ajax(
            {
                type: "POST",
                url:"/contact",
                data: JSON.stringify({
                    name:$("#name").val(),
                    email:$("#email").val(),
                    message:$("#message").val()
                }),
                success: function(data){
                    name = $("#name").val();
                    email = $("#email").val();
                    message = $("#message").val();
                    var output = "name: "+name+", email: "+email+", message: "+message;
                    console.log(output);
                    $("#name").val("");
                    $("#email").val("");
                    $("#message").val("");
                },
                dataType: 'json',
                contentType: "application/json; charset=utf-8",
             }
             );
        });
    });
