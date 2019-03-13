import React from "react";


function Comment(props) {
  return <div className="comment">
        <span><h5>{props.comment_body}</h5></span>
        <p>Comment posted by: {props.commenter}</p>
        <p>Comment posted at: {props.time}</p>
        </div>;
}

export default Comment;