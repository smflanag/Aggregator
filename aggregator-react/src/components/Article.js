import React from "react";

function Article(props) {
  return <div className="article">
        <span>{props.article_name}</span>
    </div>;
}

export default Article;