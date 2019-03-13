import React from "react";
import Comment from "./Comment";

function CommentList(props) {
  return (
    <div>
        {props.comments.map(c => <Comment key={c.id} id={c.id} comment_body={c.comment_body} commenter={c.commenter.user.username} time={c.time} />)}
        </div>
  );
}

export default CommentList;
