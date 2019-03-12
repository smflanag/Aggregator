import React, { Component } from "react";
import axios from 'axios';
import TopicList from "./components/TopicList";

class TopicCollection extends Component {
    // default State object
    state = {
    topics: []
  };
    componentDidMount() {
    axios
      .get("http://127.0.0.1:8000/topics/")
      .then(response => {

        // create an array of contacts only with relevant data
        const newTopics = response.data.map(t => {
          return {
            id: t.id,
            topic_name: t.topic_name
          };
        });

        // create a new "State" object without mutating
        // the original State object.
        const newState = Object.assign({}, this.state, {
          topics: newTopics
        });

        // store the new state object in the component's state
        this.setState(newState);
      })
      .catch(error => console.log(error));
  }

  render() {
    return (
            <div>
                <div className="page-header">
                    <h2>What topic would you like to explore?</h2>
                </div>
                <div>
                    <TopicList topics={this.state.topics} />
                </div>
            </div>
    );
  }
}


export default TopicCollection;