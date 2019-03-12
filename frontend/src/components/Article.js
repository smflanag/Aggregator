import React from "react";
import {Link
} from "react-router-dom";

function Article(props) {
    let slug_name = props.article_name.replace(/ /g,"-")
  return <div className="article">
        <Link to={`/articles/${props.id}`}>{props.article_name}</Link>
        </div>;
}

export default Article;