import React, { Component } from 'react';
import ArticleList from './ArticleList';
import axios from 'axios';


class TopicDetail extends Component {
    state = {
    articles: []};
    componentDidMount() {
        this.setState({loaded:false});
        axios
        .get("http://127.0.0.1:8000/topic_detail/" + this.props.match.params.topicId)
        .then(response => {

            const newArticles = response.data;
            this.setState({articles:newArticles});
            this.setState({loaded:true})
        })
        .catch(error => console.log(error));
    };
  render() {
    if (!this.state.loaded) {
        return <em>Loading...</em>;
    } else {
      return (

        <div>
            <div className="page-header">
                <h2>Articles in this topic include:</h2>
            </div>
            <div>
                <ArticleList articles={this.state.articles} />
            </div>
        </div>
      );
  }}
}

export default TopicDetail;