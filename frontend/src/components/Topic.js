import React from "react";
import {Link} from "react-router-dom";


function Topic(props) {
    let slug_name = props.topic_name.replace(/ /g,"-")
  return <div className="topic">
        <Link to={`/topics/${slug_name}`}>{props.topic_name}</Link>
    </div>;
}

export default Topic;