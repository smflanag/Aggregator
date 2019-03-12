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
      .get("http://127.0.0.1:8000/articles/")
      .then(response => {

        // create an array of contacts only with relevant data
        const newArticles = response.data.map(a => {
          return {
            id: a.id,
            article_name: a.article_name
          };
        });

        // create a new "State" object without mutating
        // the original State object.
        const newState = Object.assign({}, this.state, {
          articles: newArticles
        });

        // store the new state object in the component's state
        this.setState(newState);
      })
      .catch(error => console.log(error));
  }

  render() {
    return (
      <div>
        <ArticleList articles={this.state.articles} />
      </div>
    );
  }
}


export default ArticleCollection;

