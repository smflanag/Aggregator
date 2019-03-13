import React from "react";
import Topic from "./Topic";

function TopicList(props) {
  return (
    <div>
        {props.topics.map(t => <Topic key={t.id} id={t.id} topic_name={t.topic_name} />)}
        </div>
  );
}

export default TopicList;