import React from "react";
import {Link
} from "react-router-dom";

function Article(props) {
  return <div className="article">
        <Link to={`/articles/${props.id}`}>{props.article_name}</Link>
        </div>;
}

export default Article;