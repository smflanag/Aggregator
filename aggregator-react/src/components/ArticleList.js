import React from "react";
import Article from "./Article";

function ArticleList(props) {
  return (
    <div>
        {props.articles.map(a => <Article key={a.id} article_name={a.article_name} />)}
        </div>
  );
}

export default ArticleList;