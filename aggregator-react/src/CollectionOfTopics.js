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
            const newTopics = response.data;
            // store the new state object in the component's state
            this.setState({topics: newTopics});
        })
        .catch(error => console.log(error));
    };

  render() {
    return (
      <div>
        <TopicList topics={this.state.topics} />
      </div>
    );
  }
}


export default TopicCollection;