import React, { Component } from 'react';
import axios from 'axios';


class ArticleDetail extends Component {
    state = {};
    componentDidMount() {
        this.setState({loaded:false});
        axios
        .get("http://127.0.0.1:8000/api/articles/" + this.props.match.params.articleId+"/")
        .then(response => {
            const article = response.data;
            this.setState(article);
            this.setState({loaded:true})
        })
        .catch(error => console.log(error));
    };
  render() {
    if (!this.state.loaded) {
        return <em>Loading...</em>;
    } else {
      return (

        <div className="ui card">
            <div className="content">
                <p className="header">
                    <b>Name: </b>
                    {this.state.article_name}</p>
                <p><b>Posted by: </b>{this.state.created_by.user.username}</p>
                <p>{this.state.article_content}</p>

            </div>
        </div>
      );
  }}
}

export default ArticleDetail;