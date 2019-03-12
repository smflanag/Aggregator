import React, { Component } from 'react';
import ArticleList from './ArticleList';
import axios from 'axios';


class TopicDetail extends Component {
    state = {
    articles: []};
    componentDidMount() {
        this.setState({loaded1:false});
        this.setState({loaded2:false});
        axios
        .get("http://127.0.0.1:8000/topic_detail/" + this.props.match.params.topicId)
        .then(response => {
            const newArticles = response.data;
            this.setState({articles:newArticles});
            this.setState({loaded1:true})
        })
        .catch(error => console.log(error));
        axios
            .get("http://127.0.0.1:8000/topics/"+this.props.match.params.topicId+"/")
            .then( response => {
            const this_topic_name = response.data.topic_name;
            const this_topic_desc = response.data.topic_description;
            this.setState({this_topic_name:this_topic_name, this_topic_desc:this_topic_desc});
            this.setState({loaded2:true})})
    };
  render() {
    if (!this.state.loaded1 || !this.state.loaded2) {
        return <em>Loading...</em>;
    } else {
      return (

        <div>
            <div className="page-header">
                <h1>{this.state.this_topic_name}</h1>
                <h3>{this.state.this_topic_desc}</h3>
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