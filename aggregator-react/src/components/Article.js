import React from "react";
import { Link } from 'react-router-dom';

function Article(props) {
  return <div className="article">
            <div>
                <div>
                    <Link to={`/articles/${props.id}`}>{props.article_name}</Link>
                </div>
                <div>
                    <h6>Topic: {props.topic_name}</h6>
                </div>

                <div>
                    <h6>Created at: {props.created_at}</h6>
                </div>
            </div>
        </div>


}

export default Article;