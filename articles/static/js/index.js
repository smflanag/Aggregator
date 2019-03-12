//import React from 'react'
//import ReactDOM from 'react-dom'
//
//import {
//  Route,
//  NavLink,
//  HashRouter
//} from "react-router-dom";
//
//
//class Home extends React.Component {
////    componentDidMount() {
////    $.ajax(
////        {
////            type: "GET",
////            url: "/article_list",
////            success: function(response){
////                topicList.setState("topics", response);
////                    }
////            },
////            dataType: 'json',
////            contentType: "application/json; charset=utf-8"
////         );}
//  render() {
//    return (
//      <div>
//        <h2>HELLO</h2>
//        <p>Cras facilisis urna ornare ex volutpat, et
//        convallis erat elementum. Ut aliquam, ipsum vitae
//        gravida suscipit, metus dui bibendum est, eget rhoncus nibh
//        metus nec massa. Maecenas hendrerit laoreet augue
//        nec molestie. Cum sociis natoque penatibus et magnis
//        dis parturient montes, nascetur ridiculus mus.</p>
//
//        <p>Duis a turpis sed lacus dapibus elementum sed eu lectus.</p>
//      </div>
//    );
//  }
//}
//
//export default Home;
//
//class TopicList extends React.Component {
//    componentDidMount() {
//        var topicList = this;
//        $.ajax(
//            {
//                type: "GET",
//                url: "/topics",
//                success: function(response){
//                    topicList.setState("topics", response);
//                },
//                dataType: 'json',
//                contentType: "application/json; charset=utf-8",
//             }
//         );
//    }
//
//    render() {
//        var list = window.props;
//        return (
////            { props.isLoggedIn ? <div>welcome</div> : null; }
//            <div>{list.map(item =>
//                    <TopicListItem key={item.id} topic={item.topic_name}
////                    isLoggedIn={this.props.isLoggedIn}
//                    /> )}</div>)
//    }
//}
//
//
//
//
//class TopicListItem extends React.Component {
//    render() {
//        return <li><b>{this.props.topic}</b></li>;
//    }
//}
//
//class ArticleList extends React.Component {
//    componentDidMount() {
//        var articleList = this;
//        $.ajax(
//            {
//                type: "GET",
//                url: "/articles",
//                success: function(response){
//                    articleList.setState(("articles", response));
//                },
//                dataType: 'json',
//                contentType: "application/json; charset=utf-8",
//             }
//         );
//    }
//
//    render() {
//        var list = window.props;
//        return (
////            { props.isLoggedIn ? <div>welcome</div> : null; },
//            <div>
//                {list.map(item =>
//                    <ArticleListItem key={item.id} article={item.article_name}
////                    isLoggedIn={this.props.isLoggedIn}
//                    /> )
//                }
//            </div>)
//    }
//}
//
//class ArticleListItem extends React.Component {
//    render() {
//        return (
//        <HashRouter>
//            <li>
//                <b>
////                <NavLink to="{this.props.article}">
//                    {this.props.article}
////                </NavLink>
//                </b>
////                <div>
////                    <Route path="/{this.props.article}" component={ArticleList}/>
////                </div>
//            </li>
//
//        </HashRouter>
//        );
//
//
//
//
//    }
//}
//
//
//
//
//class AggregatorApp extends React.Component {
//    componentDidMount() {
//      this.setState("username", window.username);
//      this.setState("", window.user_id);
//      this.setState("isLoggedIn", window.isLoggedIn);
//    }
//
//    render() {
//        return (
//            <ArticleList
//                isLoggedIn={this.state.isLoggedIn}
//                username={this.state.username}
//                userId={this.state.userId}
//            />)
//    }
//}
//
//ReactDOM.render(
//    <ArticleList />,
//    window.react_mount
//
//);