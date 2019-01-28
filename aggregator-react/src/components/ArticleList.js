import React from "react";
import Article from "./Article";

function ArticleList(props) {
  return (
    <div>
        {props.articles.map(a => <Article id={a.id} key={a.id} article_name={a.article_name} topic_name={a.topic.topic_name} created_at={a.created_at} />)}
        </div>
  );
}

export default ArticleList;