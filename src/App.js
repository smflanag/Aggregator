import React, { Component } from 'react';

import ArticleCollection from "./CollectionOfArticles";
import TopicCollection from "./CollectionOfTopics";
import Home from "./Home";
//import Aggregator from "./src/components/Aggregator";
import TopicDetail from "./components/TopicDetail";
import ArticleDetail from "./components/ArticleDetail";
import {
  Route,
  NavLink,
  BrowserRouter
} from "react-router-dom";

class App extends Component {

  render() {
    return (
    <div className="App">

        <BrowserRouter>
            <div>

              <ul className="header">
                <li className="home"><NavLink to="/">Aggregator</NavLink></li>
                <li><NavLink to="/articles">Articles</NavLink></li>
                <li><NavLink to="/topics">Topics</NavLink></li>

              </ul>

                  <Route exact path="/" component={Home} />
                  <Route exact path="/articles" component={ArticleCollection} />
                  <Route exact path="/topics" component={TopicCollection} />

                  <Route exact path={`/articles/:articleId`} component={ArticleDetail}/>
                  <Route exact path={`/topics/:topicId`} component={TopicDetail}/>
            </div>
      </BrowserRouter>

     </div>
    );
  }
}

export default App;
