import React, { Component } from 'react';
import './App.css';
import ArticleCollection from "./CollectionOfArticles";
import TopicCollection from "./CollectionOfTopics";
import Aggregator from "./components/Aggregator";
import TopicDetail from "./components/TopicDetail";
import ArticleDetail from "./components/ArticleDetail";
import {
  Route,
  NavLink,
  HashRouter
} from "react-router-dom";

import { createStore, applyMiddleware } from "redux";
import thunk from "redux-thunk";
import { Provider } from "react-redux";
import aggregatorApp from "./reducers";

let store = createStore(aggregatorApp, applyMiddleware(thunk));


class App extends Component {

  render() {
    return (
    <div className="App">
        <header className="App-header">
          <h1 className="App-title">Aggregator</h1>
        </header>
        <Provider store={store}>
        <HashRouter>
            <div>
              <ul className="header">
                <li><NavLink to="/">Home</NavLink></li>
                <li><NavLink to="/apitest">Aggregator</NavLink></li>
                <li><NavLink to="/topics">Topic List</NavLink></li>
              </ul>
              <div className="content">
                <Route exact path={`/articles/:articleId`} component={ArticleDetail}/>
                <Route exact path="/" component={ArticleCollection}/>
                <Route exact path={`/topics/:topicId`} component={TopicDetail}/>
                <Route exact path="/topics" component={TopicCollection}/>
                <Route exact path="/apitest" component={Aggregator}/>
              </div>
            </div>
        </HashRouter>
        </Provider>
     </div>
    );
  }
}

export default App;


