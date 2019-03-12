import React, { Component } from 'react';

import ArticleCollection from "./CollectionOfArticles";
import TopicCollection from "./CollectionOfTopics";
//import Aggregator from "./src/components/Aggregator";
//import TopicDetail from "../../../src/components/TopicDetail";
//import ArticleDetail from "../../../src/components/ArticleDetail";
import {
  Route,
  NavLink,
  HashRouter
} from "react-router-dom";





class App extends Component {

  render() {
    return (
    <div className="App">
        <header className="App-header">
          <h1 className="App-title">Aggregator</h1>
        </header>
        <HashRouter>
            <div>
              <ul className="header">
                <li><NavLink to="/">Home</NavLink></li>
                <li><NavLink to="/apitest">Aggregator</NavLink></li>
                <li><NavLink to="/topics">Topic List</NavLink></li>
              </ul>
              <div className="content">
                <Route exact path="/" component={ArticleCollection}/>
                <Route exact path="/topics" component={TopicCollection}/>
              </div>
            </div>
        </HashRouter>
     </div>
    );
  }
}

export default App;
