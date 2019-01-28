import React from "react";
import Topic from "./Topic";

function TopicList(props) {
  return (
    <div>
        {props.topics.map(t => <Topic id={t.id} key={t.id} topic_name={t.topic_name} />)}
        </div>
  );
}

export default TopicList;