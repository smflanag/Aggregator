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
      .get("/topics/")
      .then(response => {
        const newTopics = response.data;
        this.setState({topics:newTopics});
        })
      .catch(error => console.log(error));
  };


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