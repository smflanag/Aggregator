import React, { Component } from 'react';

import ArticleCollection from "./CollectionOfArticles";
import TopicCollection from "./CollectionOfTopics";
import Home from "./Home";
import MyPosts from "./MyPosts";
import NewPost from './NewPost';
import Login from "./Login";
import Register from "./Register";
import TopicDetail from "./components/TopicDetail";
import ArticleDetail from "./components/ArticleDetail";
import {
  Route,
  NavLink,
  BrowserRouter,
  Redirect,
} from "react-router-dom";

class App extends Component {
      state = {};


  PrivateRoute = ({component: ChildComponent, ...rest}) => {
    return <Route {...rest} render={state => {
      if (!window.token === "") {
        return <em>Loading...</em>;
      } else if (!window.token || window.token === null) {
        return <Redirect to="/login" />;
      } else {
        return <ChildComponent {...state} />
      }
    }} />
  }



  render() {
    let {PrivateRoute} = this;
    return (
    <div className="App">

        <BrowserRouter>
            <div>

              <ul className="header">
                <li className="home"><NavLink to="/">Aggregator</NavLink></li>
                <li><NavLink to="/articles">Articles</NavLink></li>
                <li><NavLink to="/topics">Topics</NavLink></li>
                <li><NavLink to="/login">Login</NavLink></li>
                <li><NavLink to="/register">Register</NavLink></li>
                <li><NavLink to="/myposts">MyPosts</NavLink></li>

              </ul>

                  <Route exact path="/" component={Home} />
                  <Route exact path="/articles" component={ArticleCollection} />
                  <Route exact path="/topics" component={TopicCollection} />
                  <Route exact path="/login" component={Login}/>
                  <Route exact path="/register" component={Register} />
                  <PrivateRoute exact path="/myposts" component={MyPosts} />

                  <PrivateRoute exact path="/newpost" component={NewPost}/>
                  <Route exact path={`/articles/:articleId`} component={ArticleDetail}/>
                  <Route exact path={`/topics/:topicId`} component={TopicDetail}/>
            </div>
      </BrowserRouter>

     </div>
    );
  }
}

export default App;
