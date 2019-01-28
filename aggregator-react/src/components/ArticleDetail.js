import React, { Component } from 'react';
import axios from 'axios';
import CommentList from "./CommentList";


class ArticleDetail extends Component {
    state = {
    comments: []
  };
    componentDidMount() {
        axios
        .get("http://127.0.0.1:8000/article_details/" + this.props.match.params.articleId)
        .then(response => {
            const newComments = response.data;
            // store the new state object in the component's state

            this.setState({comments: newComments});




        })
        .catch(error => console.log(error));
    };
  render() {

      return (
        <div>
            <div>Name of Article should go here</div>
            <div>Article Content should go here</div>
            <span><CommentList comments={this.state.comments} /></span>
        </div>
      );
  }
}

export default ArticleDetail;