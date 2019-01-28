import React, { Component } from 'react';
import axios from 'axios';
import ArticleList from "./ArticleList";


class TopicDetail extends Component {
    state = {
    articles: []
  };
    componentDidMount() {
        axios
        .get("http://127.0.0.1:8000/topic_detail/" + this.props.match.params.topicId)
        .then(response => {
            const newArticles = response.data;
            // store the new state object in the component's state
            this.setState({articles:newArticles});
        })
        .catch(error => console.log(error));
    };
  render() {
      return (
        <div>
            <div>Name of Topic should go here</div>
            <div>Topic Description should go here</div>
            <span><ArticleList articles={this.state.articles} /></span>
        </div>
      );
  }
}

export default TopicDetail;