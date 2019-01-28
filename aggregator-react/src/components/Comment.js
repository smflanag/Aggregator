import React from "react";

function Comment(props) {
  return (
    <div className="comment">
        <span><ul><li>Time: {props.time}</li>
                <li>Comment: {props.comment_body}</li>
                <li>Article: {props.article_name}</li>
            </ul>
        </span>
    </div>)
}

export default Comment;