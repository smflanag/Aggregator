import React from "react";
import Comment from "./Comment";

function CommentList(props) {
  return (
    <div>
        {props.comments.map(c => <Comment id={c.id} key={c.id} comment_body={c.comment_body} time={c.time} article_name={c.article.article_name}/>)}
        </div>
  );
}

export default CommentList;