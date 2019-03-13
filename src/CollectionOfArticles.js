import React, { Component } from "react";
import axios from 'axios';
import ArticleList from "./components/ArticleList";

class ArticleCollection extends Component {
    // default State object
    state = {
    articles: []
  };

    componentDidMount() {
    axios
      .get("/articles/")
      .then(response => {
        const newArticles = response.data;
        this.setState({articles:newArticles});
        })
      .catch(error => console.log(error));
  };

  render() {
    return (
        <div>
            <div className="page-header">
                <h2>What article would you like to read?</h2>
            </div>
            <div>
                <ArticleList articles={this.state.articles} />
            </div>
        </div>
    );
  }
}


export default ArticleCollection;

