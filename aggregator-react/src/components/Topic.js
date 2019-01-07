import React from "react";

function Topic(props) {
  return <div className="topic">
        <span>{props.topic_name}</span>
    </div>;
}

export default Topic;