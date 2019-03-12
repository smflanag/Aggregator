import React, { Component } from 'react';
import axios from 'axios';
import CommentList from './CommentList';


class ArticleDetail extends Component {
        state = {
    comments: []};
    componentDidMount() {
        this.setState({loaded1:false});
        this.setState({loaded2:false});
        axios
        .get("http://127.0.0.1:8000/api/articles/" + this.props.match.params.articleId+"/")
        .then(response => {
            const article = response.data;
            this.setState(article);
            this.setState({loaded1:true})
        })
        .catch(error => console.log(error));
        axios
        .get("http://127.0.0.1:8000/articles/" + this.props.match.params.articleId+"/comment")
        .then(response => {
            const newComments = response.data;
            this.setState({comments:newComments});
            this.setState({loaded2:true})
        })
        .catch(error => console.log(error));
    };
  render() {
    if (!this.state.loaded1 || !this.state.loaded2) {
        return <em>Loading...</em>;
    } else {
      return (

        <div className="ui card">
            <div className="content">
                <p className="header">
                    <b>Article Title: </b>
                    {this.state.article_name}</p>
                <p><b>Posted by: </b>{this.state.created_by.user.username}</p>
                <p>{this.state.article_content}</p>
                <div>
                    <h3>Comments:</h3>
                </div>
                <div>
                    <CommentList comments={this.state.comments} />
                </div>
            </div>


        </div>
      );
  }}
}

export default ArticleDetail;