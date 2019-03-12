import React from "react";
import Article from "./Article";

function ArticleList(props) {
  return (
    <div>
        {props.articles.map(a => <Article key={a.id} id={a.id} article_name={a.article_name} created_at={a.created_at}  article_content={a.article_content} created_by={a.created_by.user.username} topic={a.topic.topic_name} />)}
        </div>
  );
}

export default ArticleList;
