import React from "react";
import {Link} from "react-router-dom";


function Topic(props) {
  return <div className="topic">
        <Link to={`/topics/${props.id}`}>{props.topic_name}</Link>
    </div>;
}

export default Topic;